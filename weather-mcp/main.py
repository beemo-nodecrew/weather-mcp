"""
기상청 단기예보 API 기반 MCP 서버

기상청의 VilageFcstInfoService_2.0 API를 사용하여 다음 기능들을 제공합니다:
- 현재 날짜와 시간 반환
- 초단기실황조회 (getUltraSrtNcst)
- 초단기예보조회 (getUltraSrtFcst)
- 단기예보조회 (getVilageFcst)
"""

import asyncio
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json
from pathlib import Path

# dotenv 로드를 위한 임포트
from dotenv import load_dotenv

# .env 파일 로드 (현재 디렉토리에서 .env 파일 찾기)
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# MCP SDK가 설치된 경우를 위한 경로 추가
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    # 로컬 개발환경용 fallback
    sys.path.append(os.path.join(os.path.dirname(__file__), "../python-sdk/src"))
    from mcp.server.fastmcp import FastMCP

from pydantic import BaseModel, Field
import httpx

# MCP 서버 생성
mcp = FastMCP("기상청 날씨 서비스")

# 기상청 API 기본 정보
WEATHER_API_BASE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
SERVICE_KEY = os.getenv("WEATHER_SERVICE_KEY")

if not SERVICE_KEY:
    print("경고: WEATHER_SERVICE_KEY 환경변수가 설정되지 않았습니다.")
    print(
        "기상청 API를 사용하려면 공공데이터포털에서 발급받은 서비스키를 설정해주세요."
    )
    print("프로젝트 루트에 .env 파일을 생성하고 다음과 같이 설정하세요:")
    print("WEATHER_SERVICE_KEY=your_api_key_here")


# 데이터 모델 정의
class WeatherResponse(BaseModel):
    """기상청 API 응답 모델"""

    resultCode: str = Field(description="응답코드")
    resultMsg: str = Field(description="응답메시지")
    dataType: str = Field(description="데이터 타입")
    numOfRows: int = Field(description="한 페이지 결과 수")
    pageNo: int = Field(description="페이지 번호")
    totalCount: int = Field(description="총 데이터 개수")
    items: List[Dict[str, Any]] = Field(description="날씨 데이터 목록")


class CurrentDateTime(BaseModel):
    """현재 날짜/시간 모델"""

    currentDate: str = Field(description="현재 날짜 (YYYY-MM-DD)")
    currentTime: str = Field(description="현재 시간 (HH:MM:SS)")
    currentDatetime: str = Field(description="현재 날짜시간 (YYYY-MM-DD HH:MM:SS)")
    baseDate: str = Field(description="기상청 API용 날짜 (YYYYMMDD)")
    baseTime: str = Field(description="기상청 API용 시간 (HHMM)")
    timezone: str = Field(description="시간대")


# 카테고리 코드 설명
CATEGORY_DESCRIPTIONS = {
    # 초단기실황
    "PTY": "강수형태 (0:없음, 1:비, 2:비/눈, 3:눈, 5:빗방울, 6:빗방울눈날림, 7:눈날림)",
    "REH": "습도 (%)",
    "RN1": "1시간 강수량 (mm)",
    "T1H": "기온 (℃)",
    "UUU": "동서바람성분 (m/s)",
    "VVV": "남북바람성분 (m/s)",
    "WSD": "풍속 (m/s)",
    # 초단기예보
    "LGT": "낙뢰 (0:없음, 1:있음)",
    "SKY": "하늘상태 (1:맑음, 3:구름많음, 4:흐림)",
    # 단기예보
    "POP": "강수확률 (%)",
    "PCP": "1시간 강수량 (mm)",
    "SNO": "1시간 신적설 (cm)",
    "TMP": "1시간 기온 (℃)",
    "TMN": "일 최저기온 (℃)",
    "TMX": "일 최고기온 (℃)",
    "WAV": "파고 (M)",
}


def get_current_base_time(api_type: str = "ncst") -> tuple[str, str]:
    """
    현재 시간을 기준으로 기상청 API에 맞는 발표일자/시각을 계산

    Args:
        api_type: API 유형 ("ncst": 초단기실황, "fcst": 초단기예보, "vilage": 단기예보)

    Returns:
        (base_date, base_time) 튜플
    """
    now = datetime.now()

    if api_type == "ncst":
        # 초단기실황: 매시각 40분에 발표 (10분 후 호출 가능)
        if now.minute < 50:
            base_time = now.replace(minute=0, second=0, microsecond=0) - timedelta(
                hours=1
            )
        else:
            base_time = now.replace(minute=0, second=0, microsecond=0)
        return base_time.strftime("%Y%m%d"), base_time.strftime("%H00")

    elif api_type == "fcst":
        # 초단기예보: 매시각 30분 발표 (45분 후 호출 가능)
        if now.minute < 45:
            base_time = now.replace(minute=30, second=0, microsecond=0) - timedelta(
                hours=1
            )
        else:
            base_time = now.replace(minute=30, second=0, microsecond=0)
        return base_time.strftime("%Y%m%d"), base_time.strftime("%H%M")

    elif api_type == "vilage":
        # 단기예보: 02, 05, 08, 11, 14, 17, 20, 23시 발표 (10분 후 호출 가능)
        forecast_hours = [2, 5, 8, 11, 14, 17, 20, 23]
        current_hour = now.hour

        suitable_hour = None
        for hour in reversed(forecast_hours):
            if current_hour >= hour:
                if current_hour == hour and now.minute >= 10:
                    suitable_hour = hour
                    break
                elif current_hour > hour:
                    suitable_hour = hour
                    break

        if suitable_hour is None:
            base_time = (now - timedelta(days=1)).replace(
                hour=23, minute=0, second=0, microsecond=0
            )
        else:
            base_time = now.replace(
                hour=suitable_hour, minute=0, second=0, microsecond=0
            )

        return base_time.strftime("%Y%m%d"), base_time.strftime("%H00")

    return now.strftime("%Y%m%d"), now.strftime("%H00")


async def call_weather_api(endpoint: str, params: Dict[str, Any]) -> WeatherResponse:
    """
    기상청 API 호출

    Args:
        endpoint: API 엔드포인트
        params: 요청 파라미터

    Returns:
        WeatherResponse 객체
    """
    if not SERVICE_KEY:
        raise ValueError("WEATHER_SERVICE_KEY 환경변수가 설정되지 않았습니다.")

    # 기본 파라미터 설정
    default_params = {
        "serviceKey": SERVICE_KEY,
        "dataType": "JSON",
        "numOfRows": "100",
        "pageNo": "1",
    }

    # 파라미터 병합
    api_params = {**default_params, **params}

    url = f"{WEATHER_API_BASE_URL}/{endpoint}"

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(url, params=api_params)
            response.raise_for_status()

            data = response.json()

            # API 응답 구조 처리
            if "response" in data:
                response_data = data["response"]
                header = response_data.get("header", {})
                body = response_data.get("body", {})

                result = WeatherResponse(
                    resultCode=header.get("resultCode", "99"),
                    resultMsg=header.get("resultMsg", "UNKNOWN_ERROR"),
                    dataType=body.get("dataType", "JSON"),
                    numOfRows=body.get("numOfRows", 0),
                    pageNo=body.get("pageNo", 1),
                    totalCount=body.get("totalCount", 0),
                    items=[],
                )

                # items 데이터 처리
                items_data = body.get("items", {})
                if isinstance(items_data, dict) and "item" in items_data:
                    items = items_data["item"]
                    if isinstance(items, list):
                        result.items = items
                    elif isinstance(items, dict):
                        result.items = [items]

                return result
            else:
                return WeatherResponse(
                    resultCode="99",
                    resultMsg="Invalid API response format",
                    dataType="JSON",
                    numOfRows=0,
                    pageNo=1,
                    totalCount=0,
                    items=[],
                )

        except httpx.HTTPError as e:
            raise ValueError(f"기상청 API 호출 실패: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"API 응답 파싱 실패: {str(e)}")
        except Exception as e:
            raise ValueError(f"예상치 못한 오류: {str(e)}")


@mcp.tool()
def get_current_datetime() -> CurrentDateTime:
    """현재 날짜와 시간을 반환합니다."""
    now = datetime.now()

    return CurrentDateTime(
        currentDate=now.strftime("%Y-%m-%d"),
        currentTime=now.strftime("%H:%M:%S"),
        currentDatetime=now.strftime("%Y-%m-%d %H:%M:%S"),
        baseDate=now.strftime("%Y%m%d"),
        baseTime=now.strftime("%H%M"),
        timezone="Asia/Seoul",
    )


@mcp.tool()
async def get_ultra_srt_ncst(
    nx: int, ny: int, base_date: Optional[str] = None, base_time: Optional[str] = None
) -> WeatherResponse:
    """
    초단기실황조회 - 현재 기상 실황 정보를 조회합니다.

    Args:
        nx: 예보지점 X 좌표 (격자 좌표)
        ny: 예보지점 Y 좌표 (격자 좌표)
        base_date: 발표일자 (YYYYMMDD, 생략시 자동 계산)
        base_time: 발표시각 (HHMM, 생략시 자동 계산)

    Returns:
        초단기실황 데이터

    Note:
        - 매시각 10분 이후 호출 가능
        - 제공 항목: 기온(T1H), 강수량(RN1), 습도(REH), 풍속(WSD) 등
    """
    if not base_date or not base_time:
        auto_date, auto_time = get_current_base_time("ncst")
        base_date = base_date or auto_date
        base_time = base_time or auto_time

    params = {
        "base_date": base_date,
        "base_time": base_time,
        "nx": str(nx),
        "ny": str(ny),
    }

    try:
        result = await call_weather_api("getUltraSrtNcst", params)

        # 응답 데이터에 카테고리 설명 추가
        for item in result.items:
            if "category" in item:
                category = item["category"]
                if category in CATEGORY_DESCRIPTIONS:
                    item["categoryDesc"] = CATEGORY_DESCRIPTIONS[category]

        return result
    except Exception as e:
        return WeatherResponse(
            resultCode="99",
            resultMsg=f"초단기실황조회 실패: {str(e)}",
            dataType="JSON",
            numOfRows=0,
            pageNo=1,
            totalCount=0,
            items=[],
        )


@mcp.tool()
async def get_ultra_srt_fcst(
    nx: int, ny: int, base_date: Optional[str] = None, base_time: Optional[str] = None
) -> WeatherResponse:
    """
    초단기예보조회 - 6시간 이내의 예보 정보를 조회합니다.

    Args:
        nx: 예보지점 X 좌표 (격자 좌표)
        ny: 예보지점 Y 좌표 (격자 좌표)
        base_date: 발표일자 (YYYYMMDD, 생략시 자동 계산)
        base_time: 발표시각 (HHMM, 생략시 자동 계산)

    Returns:
        초단기예보 데이터

    Note:
        - 매시각 45분 이후 호출 가능 (30분 발표 기준)
        - 제공 항목: 기온(T1H), 강수량(RN1), 하늘상태(SKY), 낙뢰(LGT) 등
    """
    if not base_date or not base_time:
        auto_date, auto_time = get_current_base_time("fcst")
        base_date = base_date or auto_date
        base_time = base_time or auto_time

    params = {
        "base_date": base_date,
        "base_time": base_time,
        "nx": str(nx),
        "ny": str(ny),
    }

    try:
        result = await call_weather_api("getUltraSrtFcst", params)

        # 응답 데이터에 카테고리 설명 추가
        for item in result.items:
            if "category" in item:
                category = item["category"]
                if category in CATEGORY_DESCRIPTIONS:
                    item["categoryDesc"] = CATEGORY_DESCRIPTIONS[category]

        return result
    except Exception as e:
        return WeatherResponse(
            resultCode="99",
            resultMsg=f"초단기예보조회 실패: {str(e)}",
            dataType="JSON",
            numOfRows=0,
            pageNo=1,
            totalCount=0,
            items=[],
        )


@mcp.tool()
async def get_vilage_fcst(
    nx: int, ny: int, base_date: Optional[str] = None, base_time: Optional[str] = None
) -> WeatherResponse:
    """
    단기예보조회 - 3일간의 상세 예보 정보를 조회합니다.

    Args:
        nx: 예보지점 X 좌표 (격자 좌표)
        ny: 예보지점 Y 좌표 (격자 좌표)
        base_date: 발표일자 (YYYYMMDD, 생략시 자동 계산)
        base_time: 발표시각 (HHMM, 생략시 자동 계산)

    Returns:
        단기예보 데이터

    Note:
        - 02, 05, 08, 11, 14, 17, 20, 23시 발표 (10분 후 호출 가능)
        - 제공 항목: 기온(TMP), 강수확률(POP), 하늘상태(SKY), 강수형태(PTY) 등
    """
    if not base_date or not base_time:
        auto_date, auto_time = get_current_base_time("vilage")
        base_date = base_date or auto_date
        base_time = base_time or auto_time

    params = {
        "base_date": base_date,
        "base_time": base_time,
        "nx": str(nx),
        "ny": str(ny),
    }

    try:
        result = await call_weather_api("getVilageFcst", params)

        # 응답 데이터에 카테고리 설명 추가
        for item in result.items:
            if "category" in item:
                category = item["category"]
                if category in CATEGORY_DESCRIPTIONS:
                    item["categoryDesc"] = CATEGORY_DESCRIPTIONS[category]

        return result
    except Exception as e:
        return WeatherResponse(
            resultCode="99",
            resultMsg=f"단기예보조회 실패: {str(e)}",
            dataType="JSON",
            numOfRows=0,
            pageNo=1,
            totalCount=0,
            items=[],
        )


@mcp.tool()
def get_grid_coordinates_info() -> Dict[str, Any]:
    """
    격자 좌표 변환 정보와 주요 지역의 격자 좌표를 제공합니다.

    Returns:
        격자 좌표 정보 및 주요 지역 좌표
    """
    return {
        "description": "기상청 격자 좌표계 정보",
        "coordinate_system": {
            "projection": "Lambert Conformal Conic",
            "grid_size": "5km",
            "origin": {"longitude": 126.0, "latitude": 38.0},
        },
        "major_cities": {
            "서울": {"nx": 60, "ny": 127},
            "부산": {"nx": 98, "ny": 76},
            "대구": {"nx": 89, "ny": 90},
            "인천": {"nx": 55, "ny": 124},
            "광주": {"nx": 58, "ny": 74},
            "대전": {"nx": 67, "ny": 100},
            "울산": {"nx": 102, "ny": 84},
            "세종": {"nx": 66, "ny": 103},
            "수원": {"nx": 60, "ny": 121},
            "춘천": {"nx": 73, "ny": 134},
            "강릉": {"nx": 92, "ny": 131},
            "청주": {"nx": 69, "ny": 106},
            "전주": {"nx": 63, "ny": 89},
            "제주": {"nx": 52, "ny": 38},
            "서귀포": {"nx": 52, "ny": 33},
        },
        "conversion_note": "경도/위도를 격자 좌표로 변환하려면 기상청에서 제공하는 변환 공식을 사용해야 합니다.",
    }


if __name__ == "__main__":
    print("기상청 날씨 MCP 서버가 시작되었습니다.")
    print("사용 가능한 도구:")
    print("- get_current_datetime: 현재 날짜/시간 조회")
    print("- get_ultra_srt_ncst: 초단기실황조회")
    print("- get_ultra_srt_fcst: 초단기예보조회")
    print("- get_vilage_fcst: 단기예보조회")
    print("- get_grid_coordinates_info: 격자 좌표 정보")
    mcp.run(transport="stdio")
