# 기상청 날씨 MCP 서버

기상청의 단기예보 조회서비스 API를 사용하는 MCP (Model Context Protocol) 서버입니다.

## 기능

- **현재 날짜/시간 조회**: 현재 시간과 기상청 API에 맞는 형식 반환
- **초단기실황조회**: 현재 기상 실황 정보 (기온, 습도, 강수량 등)
- **초단기예보조회**: 6시간 이내 예보 정보
- **단기예보조회**: 3일간 상세 예보 정보
- **격자 좌표 정보**: 주요 도시의 격자 좌표 및 변환 정보

## 설치 및 설정

### 1. 프로젝트 설정 (uv 사용)

```bash
uv sync
```

### 2. 환경변수 설정

`.env.example` 파일을 `.env`로 복사하고 기상청 API 서비스키를 설정:

```bash
cp .env.example .env
```

`.env` 파일을 열어서 서비스키를 입력:

```bash
WEATHER_SERVICE_KEY=your_actual_service_key_here
```

서비스키는 [공공데이터포털](https://www.data.go.kr)에서 발급받을 수 있습니다:

1. 공공데이터포털 회원가입
2. "기상청\_단기예보 조회서비스" 검색
3. 활용신청 후 서비스키 발급

## 사용법

### MCP 서버로 실행

```bash
uv run python main.py
```

## MCP 도구 목록

### 1. get_current_datetime

현재 날짜와 시간을 반환합니다.

### 2. get_ultra_srt_ncst

초단기실황조회 - 현재 기상 실황 정보를 조회합니다.

**파라미터:**

- `nx` (int): 예보지점 X 좌표 (격자 좌표)
- `ny` (int): 예보지점 Y 좌표 (격자 좌표)
- `base_date` (str, optional): 발표일자 (YYYYMMDD)
- `base_time` (str, optional): 발표시각 (HHMM)

### 3. get_ultra_srt_fcst

초단기예보조회 - 6시간 이내의 예보 정보를 조회합니다.

**파라미터:**

- `nx` (int): 예보지점 X 좌표 (격자 좌표)
- `ny` (int): 예보지점 Y 좌표 (격자 좌표)
- `base_date` (str, optional): 발표일자 (YYYYMMDD)
- `base_time` (str, optional): 발표시각 (HHMM)

### 4. get_vilage_fcst

단기예보조회 - 3일간의 상세 예보 정보를 조회합니다.

**파라미터:**

- `nx` (int): 예보지점 X 좌표 (격자 좌표)
- `ny` (int): 예보지점 Y 좌표 (격자 좌표)
- `base_date` (str, optional): 발표일자 (YYYYMMDD)
- `base_time` (str, optional): 발표시각 (HHMM)

### 5. get_grid_coordinates_info

격자 좌표 변환 정보와 주요 지역의 격자 좌표를 제공합니다.

## 주요 도시 격자 좌표

| 도시 | X좌표 | Y좌표 |
| ---- | ----- | ----- |
| 서울 | 60    | 127   |
| 부산 | 98    | 76    |
| 대구 | 89    | 90    |
| 인천 | 55    | 124   |
| 광주 | 58    | 74    |
| 대전 | 67    | 100   |
| 울산 | 102   | 84    |
| 세종 | 66    | 103   |

## 기상 데이터 카테고리

### 초단기실황

- **T1H**: 기온 (℃)
- **RN1**: 1시간 강수량 (mm)
- **REH**: 습도 (%)
- **PTY**: 강수형태 (0:없음, 1:비, 2:비/눈, 3:눈)
- **WSD**: 풍속 (m/s)

### 초단기예보

- **T1H**: 기온 (℃)
- **RN1**: 1시간 강수량 (mm)
- **SKY**: 하늘상태 (1:맑음, 3:구름많음, 4:흐림)
- **LGT**: 낙뢰 (0:없음, 1:있음)

### 단기예보

- **TMP**: 1시간 기온 (℃)
- **TMN**: 일 최저기온 (℃)
- **TMX**: 일 최고기온 (℃)
- **POP**: 강수확률 (%)
- **PTY**: 강수형태 (0:없음, 1:비, 2:비/눈, 3:눈, 4:소나기)
- **PCP**: 1시간 강수량 (mm)
- **SNO**: 1시간 신적설 (cm)

## API 발표 시간

- **초단기실황**: 매시각 40분 발표 (10분 후 호출 가능)
- **초단기예보**: 매시각 30분 발표 (45분 후 호출 가능)
- **단기예보**: 02, 05, 08, 11, 14, 17, 20, 23시 발표 (10분 후 호출 가능)

## 패키지 의존성

설치가 필요한 패키지:

- `httpx>=0.28.1` - HTTP 클라이언트
- `pydantic>=2.11.7` - 데이터 검증 및 직렬화
- `python-dotenv>=1.0.0` - 환경변수 관리
- `mcp[cli]>=1.10.1` - MCP 서버 프레임워크

개발용 패키지:

- `pytest>=7.0` - 테스트 프레임워크
- `pytest-asyncio>=0.21.0` - 비동기 테스트 지원

## 라이선스

MIT License

## 참고

- [기상청 단기예보 조회서비스 API](https://www.data.go.kr/iim/api/selectAPIAcountView.do?aqIdx=21057)
- [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol)
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk)
