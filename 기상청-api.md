

**기상청 단기예보 조회서비스** 

**Open API 활용가이드**

 

 

 

[**1\. 서비스 명세	3**](#1.-서비스-명세)

[**1.1 단기예보 조회서비스**	3](#1.1-단기예보-조회서비스)

[가. API 서비스 개요	3](#가.-api-서비스-개요)

[나. 상세기능 목록	4](#나.-상세기능-목록)

[다. 상세기능내역	4](#다.-상세기능내역)

[1\) \[초단기실황조회\] 상세기능명세	4](#1\)-[초단기실황조회]-상세기능명세)

[2\) \[초단기예보조회\] 상세기능명세	7](#2\)-[초단기예보조회]-상세기능명세)

[3\) \[단기예보조회\] 상세기능명세	10](#3\)-[단기예보조회]-상세기능명세)

[4\) \[예보버전조회\] 상세기능명세	13](#4\)-[예보버전조회]-상세기능명세)

[**2\. 참고자료	16**](#2.-참고자료)

**1\. 서비스 명세**

**1.1 단기예보 조회서비스**

가. API 서비스 개요

| API 서비스 정보 | API명(영문) | VilageFcstInfoService\_2.0 |  |  |
| :---: | :---: | :---- | :---: | :---- |
|  | **API명(국문)** | 단기예보 조회서비스(2.0) |  |  |
|  | **API 설명** | 초단기실황, 초단기예보, 단기예보, 예보버전 정보를 조회하는 서비스입니다. 초단기실황정보는 예보 구역에 대한 대표 AWS 관측값을, 초단기예보는 예보시점부터 6시간 이내의 예보를, 단기예보는 예보기간과 구역을 시공간적으로 세분화한 예보를 제공합니다. |  |  |
| **API 서비스 보안적용 기술 수준** | **서비스 인증/권한** | \[O\] ServiceKey    \[ \] 인증서 (GPKI/NPKI) \[ \] Basic (ID/PW)  \[ \] 없음 |  |  |
|  | **메시지 레벨 암호화** | \[ \] 전자서명   \[ \] 암호화   \[O\] 없음 |  |  |
|  | **전송 레벨 암호화** | \[ \] SSL   \[O\] 없음 |  |  |
|  | **인터페이스 표준** | \[ \] SOAP 1.2 (RPC-Encoded, Document Literal, Document Literal Wrapped) \[O\] REST (GET) \[ \] RSS 1.0   \[ \] RSS 2.0   \[ \] Atom 1.0   \[ \] 기타 |  |  |
|  | **교환 데이터 표준 (중복선택가능)** | \[O\] XML   \[O\] JSON   \[ \] MIME   \[ \] MTOM |  |  |
| **API 서비스 배포정보** | **서비스 URL** | http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0 |  |  |
|  | **서비스 명세 URL (WSDL 또는 WADL)** | N/A |  |  |
|  | **서비스 버전** | 1.0 |  |  |
|  | **서비스 시작일** | 2021-07-01 | **서비스 배포일** | 2021-07-01 |
|  | **서비스 이력** | 2021-07-01 : 서비스 시작 |  |  |
|  | **메시지 교환유형** | \[O\] Request-Response   \[ \] Publish-Subscribe \[ \] Fire-and-Forgot   \[ \] Notification |  |  |
|  | **데이터 갱신주기** | 수시 (일 8회) |  |  |

나. 상세기능 목록

| 번호 | API명(국문) | 상세기능명(영문) | 상세기능명(국문) |
| :---: | :---: | :---: | :---: |
| 1 | 단기예보 조회서비스 | getUltraSrtNcst | 초단기실황조회 |
| 2 |  | getUltraSrtFcst | 초단기예보조회 |
| 3 |  | getVilageFcst | 단기예보조회 |
| 4 |  | getFcstVersion | 예보버전조회 |

다. 상세기능내역

1\) \[초단기실황조회\] 상세기능명세

a) 상세기능정보

| 상세기능 번호 | 1 | 상세기능 유형 | 조회 (목록) |
| :---: | ----- | :---: | ----- |
| **상세기능명(국문)** | 초단기실황조회 |  |  |
| **상세기능 설명** | 실황정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 조회 조건으로 자료구분코드, 실황값, 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능 |  |  |
| **Call Back URL** | http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getUltraSrtNcst |  |  |
| **최대 메시지 사이즈** | \[1764\] byte |  |  |
| **평균 응답 시간** | \[100\] ms | **초당 최대 트랙잭션** | \[30\] tps |

b) 요청 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| serviceKey | 인증키 | 100 | 1 | 인증키 (URL Encode) | 공공데이터포털에서 발급받은 인증키 |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 10 | 한 페이지 결과 수 Default: 10 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 번호 Default: 1 |
| dataType | 응답자료형식 | 4 | 0 | XML | 요청자료형식(XML/JSON) Default: XML |
| base\_date | 발표일자 | 8 | 1 | 20210628 | ‘21년 6월 28일 발표 |
| base\_time | 발표시각 | 4 | 1 | 0600 | 06시 발표(정시단위) \-매시각 10분 이후 호출 |
| nx | 예보지점 X 좌표 | 2 | 1 | 55 | 예보지점의 X 좌표값 **\*별첨 엑셀 자료 참조** |
| ny | 예보지점 Y 좌표 | 2 | 1 | 127 | 예보지점의 Y 좌표값 **\*별첨 엑셀 자료 참조** |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n)

c) 응답 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 1 | 한 페이지당 표출 데이터 수 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 수 |
| totalCount | 데이터 총 개수 | 10 | 1 | 1 | 데이터 총 개수 |
| resultCode | 응답메시지 코드 | 2 | 1 | 00 | 응답 메시지코드 |
| resultMsg | 응답메시지 내용 | 100 | 1 | NORMAL SERVICE | 응답 메시지 설명 |
| dataType | 데이터 타입 | 4 | 1 | XML | 응답자료형식 (XML/JSON) |
| baseDate | 발표일자 | 8 | 1 | 20210628 | ‘21년 6월 28일 발표 |
| baseTime | 발표시각 | 6 | 1 | 0600 | 06시 발표(매 정시) |
| nx | 예보지점 X 좌표 | 2 | 1 | 55 | 입력한 예보지점 X 좌표 |
| ny | 예보지점 Y 좌표 | 2 | 1 | 127 | 입력한 예보지점 Y 좌표 |
| category | 자료구분코드 | 3 | 1 | RN1 | 자료구분코드  \* 하단 코드값 정보 참조 |
| obsrValue | 실황 값 | 2 | 1 | 0 | RN1, T1H, UUU, VVV, WSD  실수 또는 정수로 제공 **\* 하단 코드값 정보 참조** |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n), 코드표별첨

d) 요청/응답 메시지 예제

| 요청메시지 |
| ----- |
| http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getUltraSrtNcst?serviceKey=인증키&numOfRows=10\&pageNo=1\&base\_date=20210628\&base\_time=0600\&nx=55\&ny=127 |
| **응답메시지** |
| \<?xml version\="1.0" encoding\="UTF-8"?\> \<response\>     \<header\>         \<resultCode\>0\</resultCode\>         \<resultMsg\>NORMAL\_SERVICE\</resultMsg\>     \</header\>     \<body\>         \<dataType\>XML\</dataType\>         \<items\>             \<item\>                 \<baseDate\>20210628\</baseDate\>                 \<baseTime\>0600\</baseTime\>                 \<category\>RN1\</category\>                 \<nx\>55\</nx\>                 \<ny\>127\</ny\>                 \<obsrValue\>1.1\</obsrValue\>             \</item\>         \</items\>         \<numOfRows\>10\</numOfRows\>         \<pageNo\>1\</pageNo\>         \<totalCount\>8\</totalCount\>     \</body\> \</response\> |

2\) \[초단기예보조회\] 상세기능명세

a) 상세기능정보

| 상세기능 번호 | 2 | 상세기능 유형 | 조회 (상세) |
| :---: | ----- | :---: | ----- |
| **상세기능명(국문)** | 초단기예보조회 |  |  |
| **상세기능 설명** | 초단기예보정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 조회 조건으로 자료구분코드, 예보값, 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능 |  |  |
| **Call Back URL** | http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getUltraSrtFcst |  |  |
| **최대 메시지 사이즈** | \[2686\] byte |  |  |
| **평균 응답 시간** | \[100\] ms | **초당 최대 트랙잭션** | \[30\] tps |

b) 요청 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| serviceKey | 인증키 | 100 | 1 | 인증키 (URL Encode) | 공공데이터포털에서 발급받은 인증키 |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 10 | 한 페이지 결과 수 Default: 10 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 번호 Default: 1 |
| dataType | 응답자료형식 | 4 | 0 | XML | 요청자료형식(XML/JSON) Default: XML |
| base\_date | 발표일자(필수) | 8 | 1 | 20210628 | ‘21년 6월 28일 발표(필수) |
| base\_time | 발표시각(필수) | 4 | 1 | 0630 | 06시30분 발표(30분 단위) (필수) \- 매시각 45분 이후 호출 |
| nx | 예보지점 X 좌표(필수) | 2 | 1 | 55 | 예보지점 X 좌표값(필수) **\*별첨 엑셀 자료 참조** |
| ny | 예보지점 Y 좌표(필수) | 2 | 1 | 127 | 예보지점 Y 좌표값(필수) **\*별첨 엑셀 자료 참조** |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n)

c) 응답 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 1 | 한 페이지당 표출 데이터 수 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 수 |
| totalCount | 데이터 총 개수 | 10 | 1 | 1 | 데이터 총 개수 |
| resultCode | 응답메시지 코드 | 2 | 1 | 00 | 응답 메시지코드 |
| resultMsg | 응답메시지 내용 | 100 | 1 | NORMAL SERVICE | 응답 메시지 설명 |
| dataType | 데이터 타입 | 4 | 1 | XML | 응답자료형식 (XML/JSON) |
| baseDate | 발표일자 | 8 | 1 | 20210628 | ‘21년 6월 28일 발표 |
| baseTime | 발표시각 | 4 | 1 | 1200 | 12시00분 발표 |
| nx | 예보지점 X 좌표 | 2 | 1 | 55 | 입력한 예보지점 X 좌표 |
| ny | 예보지점 Y 좌표 | 2 | 1 | 127 | 입력한 예보지점 Y 좌표 |
| category | 자료구분코드 | 3 | 1 | LGT | 자료구분코드  \* 하단 참고자료 참조 |
| fcstDate | 예측일자 | 8 | 1 | 20210628 | 예측일자(YYYYMMDD) |
| fcstTime | 예측시간 | 4 | 1 | 1200 | 예측시간(HH24MI) |
| fcstValue | 예보 값 | 2 | 1 | 0 | 예보 값 \- Category(자료구분)에 대한 예측값 **\* 하단 참고자료 참조** |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n), 코드표별첨

d) 요청/응답 메시지 예제

| 요청메시지 |
| ----- |
| http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getUltraSrtFcst?serviceKey=인증키&numOfRows=10\&pageNo=1\&base\_date=20210628\&base\_time=0630\&nx=55\&ny=127 |
| **응답메시지** |
| \<?xml version\="1.0" encoding\="UTF-8"?\> \<response\>     \<header\>         \<resultCode\>0\</resultCode\>         \<resultMsg\>NORMAL\_SERVICE\</resultMsg\>     \</header\>     \<body\>         \<dataType\>XML\</dataType\>         \<items\>             \<item\>                 \<baseDate\>20210628\</baseDate\>                 \<baseTime\>0630\</baseTime\>                 \<category\>LGT\</category\>                 \<fcstDate\>20210628\</fcstDate\>                 \<fcstTime\>1200\</fcstTime\>                 \<fcstValue\>0\</fcstValue\>                 \<nx\>55\</nx\>                 \<ny\>127\</ny\>             \</item\>         \</items\>         \<numOfRows\>10\</numOfRows\>         \<pageNo\>1\</pageNo\>         \<totalCount\>60\</totalCount\>     \</body\> \</response\> |

3\) \[단기예보조회\] 상세기능명세

a) 상세기능정보

| 상세기능 번호 | 3 | 상세기능 유형 | 조회 (상세) |
| :---: | ----- | :---: | ----- |
| **상세기능명(국문)** | 단기예보조회 |  |  |
| **상세기능 설명** | 단기예보 정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X좌표, 예보지점 Y 좌표의 조회 조건으로 발표일자, 발표시각, 자료구분문자, 예보 값, 예보일자, 예보시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능 |  |  |
| **Call Back URL** | http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getVilageFcst |  |  |
| **최대 메시지 사이즈** | \[48,452\] byte |  |  |
| **평균 응답 시간** | \[600\] ms | **초당 최대 트랙잭션** | \[30\] tps |

b) 요청 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| serviceKey | 인증키 | 100 | 1 | 인증키 (URL Encode) | 공공데이터포털에서 발급받은 인증키 |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 50 | 한 페이지 결과 수 Default: 10 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 번호 Default: 1 |
| dataType | 응답자료형식 | 4 | 0 | XML | 요청자료형식(XML/JSON) Default: XML |
| base\_date | 발표일자 | 8 | 1 | 20210628 | ‘21년 6월 28일발표 |
| base\_time | 발표시각 | 4 | 1 | 0500 | 05시 발표 **\* 하단 참고자료 참조** |
| nx | 예보지점 X 좌표 | 2 | 1 | 55 | 예보지점의 X 좌표값 **\*별첨 엑셀 자료 참조** |
| ny | 예보지점 Y 좌표 | 2 | 1 | 127 | 예보지점의 Y 좌표값 **\*별첨 엑셀 자료 참조** |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n)

c) 응답 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 50 | 한 페이지당 표출 데이터 수 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 수 |
| totalCount | 데이터 총 개수 | 10 | 1 | 1 | 데이터 총 개수 |
| resultCode | 응답메시지 코드 | 2 | 1 | 00 | 응답 메시지코드 |
| resultMsg | 응답메시지 내용 | 100 | 1 | NORMAL SERVICE | 응답 메시지 설명 |
| dataType | 데이터 타입 | 4 | 1 | XML | 응답자료형식 (XML/JSON) |
| baseDate | 발표일자 | 8 | 1 | 20210628 | ‘21년 6월 28일 발표 |
| baseTime | 발표시각 | 6 | 1 | 0500 | 05시 발표 |
| fcstDate | 예보일자 | 8 | 1 | 20210628 | ‘21년 6월 28일 예보 |
| fcstTime | 예보시각 | 4 | 1 | 0600 | 6시 예보 |
| category | 자료구분문자 | 3 | 1 | TMP | 자료구분코드  **\* 하단 코드값 정보 참조** |
| fcstValue | 예보 값 | 2 | 1 | 21 | **\* 하단 코드값 정보 참조** \* TMP, TMN, TMX, UUU, VVV, WAV, WSD 자료는 실수 또는 정수로 제공 |
| nx | 예보지점 X 좌표 | 2 | 1 | 55 | 입력한 예보지점 X 좌표 |
| ny | 예보지점 Y 좌표 | 2 | 1 | 127 | 입력한 예보지점 Y 좌표 |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n), 코드표별첨

※ 단기예보 5일 연장으로 02·05·08·11·14시 발표기준 글피 예보, 17·20·23시 발표기준 그글피 예보제공

 \- 연장기간인 (02·05·08·11·14시 발표)글피, (17·20·23시 발표)그글피 예보는 3시간 간격의 자료를 제공하며, 강수량(PCP), 강설(SNO), 풍속(WSD) 요소는 정성정보(코드값)를 제공(코드표 참고)

d) 요청/응답 메시지 예제

| 요청메시지 |
| ----- |
| http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getVilageFcst?serviceKey=인증키&numOfRows=10\&pageNo=1\&base\_date=20210628\&base\_time=0500\&nx=55\&ny=127 |
| **응답메시지** |
| \<?xml version\="1.0" encoding\="UTF-8"?\> \<response\>     \<header\>         \<resultCode\>0\</resultCode\>         \<resultMsg\>NORMAL\_SERVICE\</resultMsg\>     \</header\>     \<body\>         \<dataType\>XML\</dataType\>         \<items\>             \<item\>                 \<baseDate\>20210628\</baseDate\>                 \<baseTime\>0500\</baseTime\>                 \<category\>TMP\</category\>                 \<fcstDate\>20210628\</fcstDate\>                 \<fcstTime\>0600\</fcstTime\>                 \<fcstValue\>21\</fcstValue\>                 \<nx\>55\</nx\>                 \<ny\>127\</ny\>             \</item\>         \</items\>         \<numOfRows\>10\</numOfRows\>         \<pageNo\>1\</pageNo\>         \<totalCount\>742\</totalCount\>     \</body\> \</response\> |

4\) \[예보버전조회\] 상세기능명세

a) 상세기능정보

| 상세기능 번호 | 4 | 상세기능 유형 | 조회 (목록) |
| :---: | ----- | :---: | ----- |
| **상세기능명(국문)** | 예보버전조회 |  |  |
| **상세기능 설명** | 단기예보정보조회서비스 각각의 오퍼레이션(초단기실황, 초단기예보, 단기예보)들의 수정된 예보 버전을 파악하기 위해 예보버전을 조회하는 기능 |  |  |
| **Call Back URL** | http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getFcstVersion |  |  |
| **최대 메시지 사이즈** | \[353\] byte |  |  |
| **평균 응답 시간** | \[100\] ms | **초당 최대 트랙잭션** | \[30\] tps |

b) 요청 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| serviceKey | 인증키 | 100 | 1 | 인증키 (URL Encode) | 공공데이터포털에서 발급받은 인증키 |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 10 | 한 페이지 결과 수 Default: 10 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 번호 Default: 1 |
| dataType | 응답자료형식 | 4 | 0 | XML | 요청자료형식(XML/JSON) Default: XML |
| ftype | 파일구분 | 5 | 1 | ODAM | 파일구분 \-ODAM: 초단기실황 \-VSRT: 초단기예보 \-SHRT: 단기예보 |
| basedatetime | 발표일시분 | 10 | 1 | 202106290800 | 각각의 base\_time 로 검색 참고자료 참조 |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n)

c) 응답 메시지 명세

| 항목명(영문) | 항목명(국문) | 항목크기 | 항목구분 | 샘플데이터 | 항목설명 |
| ----- | ----- | :---: | :---: | ----- | ----- |
| numOfRows | 한 페이지 결과 수 | 4 | 1 | 1 | 한 페이지당 표출 데이터 수 |
| pageNo | 페이지 번호 | 4 | 1 | 1 | 페이지 수 |
| totalCount | 데이터 총 개수 | 10 | 1 | 1 | 데이터 총 개수 |
| resultCode | 응답메시지 코드 | 2 | 1 | 00 | 응답 메시지코드 |
| resultMsg | 응답메시지 내용 | 100 | 1 | NORMAL SERVICE | 응답 메시지 설명 |
| dataType | 데이터 타입 | 4 | 1 | XML | 응답자료형식 (XML/JSON) |
| version | 파일버전 | 4 | 1 | 20210628092217 | 파일버전 정보 \- 파일 생성 시간 |
| filetype | 파일구분 | 5 | 1 | ODAM | 파일구분 \-ODAM: 초단기실황 \-VSRT: 초단기예보 \-SHRT: 단기예보 |

※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n), 코드표별첨

d) 요청/응답 메시지 예제

| 요청메시지 |
| ----- |
| http://apis.data.go.kr/1360000/VilageFcstInfoService\_2.0/getFcstVersion?serviceKey=인증키&numOfRows=10\&pageNo=1\&ftype=ODAM\&basedatetime=202106280800 |
| **응답메시지** |
| \<?xml version\="1.0" encoding\="UTF-8"?\> \<response\>     \<header\>         \<resultCode\>0\</resultCode\>         \<resultMsg\>NORMAL\_SERVICE\</resultMsg\>     \</header\>     \<body\>         \<dataType\>XML\</dataType\>         \<items\>             \<item\>                 \<filetype\>ODAM\</filetype\>                 \<version\>20210628092217\</version\>             \</item\>         \</items\>         \<numOfRows\>10\</numOfRows\>         \<pageNo\>1\</pageNo\>         \<totalCount\>1\</totalCount\>     \</body\> \</response\> |

**2\. 참고자료**

**\# 단기예보 연장에 따른 코드값 정보(2024.11.28. 14시\~)**

| 예보 요소 | 정성정보 코드값 | 정성정보 용어 | 정성정보 의미 |
| :---: | :---: | :---: | :---: |
| **강수량 (PCP)** | **1** | **약한 비** | 시간당 3mm 미만의 약한 비 |
|  | **2** | **보통 비** | 시간당 3mm 이상 15mm 미만의 보통 비 |
|  | **3** | **강한 비** | 시간당 15mm 이상의 강한 비 |
| **눈의양 (SNO)** | **1** | **보통 눈** | 시간당 1cm 미만의 보통 눈 |
|  | **2** | **많은 눈** | 시간당 1cm 이상의 많은 눈 |
| **풍  속 (WSD)** | **1** | **약한 바람** | 4m/s 이상의 약한 바람 |
|  | **2** | **약간 강한 바람** | 4m/s 이상 9m/s 미만의 약간 강한 바람 |
|  | **3** | **강한 바람** | 9m/s 이상의 강한 바람 |

**\# 코드값 정보**

| 예보구분 | 항목값 | 항목명 | 단위 | 압축bit수 |
| ----- | :---: | ----- | ----- | :---: |
| 단기예보 | POP | 강수확률 | % | 8 |
|  | PTY | 강수형태 | 코드값 | 4 |
|  | PCP | 1시간 강수량 | 범주 (1 mm) | 8 |
|  | REH | 습도 | % | 8 |
|  | SNO | 1시간 신적설 | 범주(1 cm) | 8 |
|  | SKY | 하늘상태 | 코드값 | 4 |
|  | TMP | 1시간 기온 | ℃ | 10 |
|  | TMN | 일 최저기온 | ℃ | 10 |
|  | TMX | 일 최고기온 | ℃ | 10 |
|  | UUU | 풍속(동서성분) | m/s | 12 |
|  | VVV | 풍속(남북성분) | m/s | 12 |
|  | WAV | 파고 | M | 8 |
|  | VEC | 풍향 | deg | 10 |
|  | WSD | 풍속 | m/s | 10 |
| 초단기실황 | T1H | 기온 | ℃ | 10 |
|  | RN1 | 1시간 강수량 | mm | 8 |
|  | UUU | 동서바람성분 | m/s | 12 |
|  | VVV | 남북바람성분 | m/s | 12 |
|  | REH | 습도 | % | 8 |
|  | PTY | 강수형태 | 코드값 | 4 |
|  | VEC | 풍향 | deg | 10 |
|  | WSD | 풍속 | m/s | 10 |
| 초단기예보 | T1H | 기온 | ℃ | 10 |
|  | RN1 | 1시간 강수량 | 범주 (1 mm) | 8 |
|  | SKY | 하늘상태 | 코드값 | 4 |
|  | UUU | 동서바람성분 | m/s | 12 |
|  | VVV | 남북바람성분 | m/s | 12 |
|  | REH | 습도 | % | 8 |
|  | PTY | 강수형태 | 코드값 | 4 |
|  | LGT | 낙뢰 | kA(킬로암페어) | 4 |
|  | VEC | 풍향 | deg | 10 |
|  | WSD | 풍속 | m/s | 10 |
| ◼ \+900이상, –900 이하 값은 **Missing 값으로 처리** 관측장비가 없는 해양 지역이거나 관측장비의 결측 등으로 자료가 없음을 의미 ◼ 압축 Bit 수의 경우 Missing 값이 아닌 경우의 기준 |  |  |  |  |

**\# 특정 요소의 코드값 및 범주**  
\- 하늘상태(SKY) 코드 : 맑음(1), 구름많음(3), 흐림(4)  
\- 강수형태(PTY) 코드 : (초단기) 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)   
                      (단기) 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4)   
\- 초단기예보, 단기예보 강수량(RN1, PCP) 범주 및 표시방법(값)

| 범주 | 문자열표시 |
| :---: | :---: |
| 0.1 \~ 1.0mm 미만 | 1mm 미만 |
| 1.0mm 이상 30.0mm 미만 | 실수값+mm (1.0mm\~29.9mm) |
| 30.0 mm 이상 50.0 mm 미만 | 30.0\~50.0mm |
| 50.0 mm 이상 | 50.0mm 이상 |

※ \-, null, 0값은 ‘강수없음’

예) PCP \= 6.2 일 경우 강수량은 6.2mm  
    PCP \= 30 일 경우 강수량은 30.0\~50.0mm

JAVA  
if(f \< 1.0f) return "1mm 미만";		  
		else if(f \>= 1.0f && f \< 30.0f) return "1.0\~29.0mm";  
		else if(f \>= 30.0f && f \< 50.0f) return "30.0\~50.0mm";  
		else return "50.0mm이상";

\- 신적설(SNO) 범주 및 표시방법(값)

| 범주 | 문자열표시 |
| :---: | :---: |
| 0.1 \~ 0.5cm 미만 | 0.5cm 미만 |
| 0.5cm 이상 5.0cm 미만 | 실수값+cm (0.5cm\~4.9cm) |
| 5.0 cm 이상 | 5.0cm 이상 |

※ \-, null, 0값은 ‘적설없음’

\- 낙뢰코드(LGT) 정보  
낙뢰(초단기예보) : 에너지밀도(0.2\~100kA(킬로암페어)/㎢)

\- 풍속 정보  
동서바람성분(UUU) : 동(+표기), 서(-표기)  
남북바람성분(VVV) : 북(+표기), 남(-표기)

❍ 단기예보조회 해상 마스킹 처리  
\- 해상에는 기온군, 강수확률, 강수량/적설, 습도를 제공하지 않음  
(Missing값으로 마스킹처리 함)

**\# 예보 발표시각**  
❍ 단기예보 발표시각  
\- Base\_time : 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 (1일 8회)  
\- API 제공 시간(\~이후) : 02:10, 05:10, 08:10, 11:10, 14:10, 17:10, 20:10, 23:10

**※ \[단기예보 발표시간 별 예보시각\]**

| 발표시각(KST) | 예보기간 |  |  |  |  |
| :---: | ----- | :---: | :---: | :---: | :---: |
|  | **\+1일** | **\+2일** | **\+3일** | **\+4일** | **\+5일** |
| 02·05·08·11·14시 | **1시간 간격** 정량값 및 정성정보 |  |  | **3시간 간격** | \- |
| 17·20·23시 |    **1시간 간격** 정량값 및 정성정보 |  |  |  | **3시간 간격** |

❍ 초단기실황 발표시각   
※ 매시간 정시에 생성되고 10분마다 최신 정보로 업데이트

| 기준 시간 | 생성시간 | Base\_time | API 제공 시간(\~이후) | 기준 시간 | 생성시간 | Base\_time | API 제공 시간(\~이후) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 00 시 | 00:00 | 0000 | 00:10 | 12 시 | 12:00 | 1200 | 12:10 |
| 01 시 | 01:00 | 0100 | 01:10 | 13 시 | 13:00 | 1300 | 13:10 |
| 02 시 | 02:00 | 0200 | 02:10 | 14 시 | 14:00 | 1400 | 14:10 |
| 03 시 | 03:00 | 0300 | 03:10 | 15 시 | 15:00 | 1500 | 15:10 |
| 04 시 | 04:00 | 0400 | 04:10 | 16 시 | 16:00 | 1600 | 16:10 |
| 05 시 | 05:00 | 0500 | 05:10 | 17 시 | 17:00 | 1700 | 17:10 |
| 06 시 | 06:00 | 0600 | 06:10 | 18 시 | 18:00 | 1800 | 18:10 |
| 07 시 | 07:00 | 0700 | 07:10 | 19 시 | 19:00 | 1900 | 19:10 |
| 08 시 | 08:00 | 0800 | 08:10 | 20 시 | 20:00 | 2000 | 20:10 |
| 09 시 | 09:00 | 0900 | 09:10 | 21 시 | 21:00 | 2100 | 21:10 |
| 10 시 | 10:00 | 1000 | 10:10 | 22 시 | 22:00 | 2200 | 22:10 |
| 11 시 | 11:00 | 1100 | 11:10 | 23 시 | 23:00 | 2300 | 23:10 |

❍초단기예보 발표시각  
※ 매시간 30분에 생성되고 10분마다 최신 정보로 업데이트(기온, 습도, 바람)

| 기준 시간 | 생성시각 | Base\_time | API 제공 시간 (\~이후) | 예보시간 (매 발표시각마다 6시간 예보) |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  | h시\~h+1시 | h+1시\~h+2시 | h+2시\~h+3시 | h+3시\~h+4시 | h+4시\~h+5시 | h+5시\~h+6시 |
| 00 시 | 00:30 | 0030 | 00:45 | 0\~1시 | 1\~2시 | 2\~3시 | 3\~4시 | 4\~5시 | 5\~6시 |
| 01 시 | 01:30 | 0130 | 01:45 | 1\~2시 | 2\~3시 | 3\~4시 | 4\~5시 | 5\~6시 | 6\~7시 |
| 02 시 | 02:30 | 0230 | 02:45 | 2\~3시 | 3\~4시 | 4\~5시 | 5\~6시 | 6\~7시 | 7\~9시 |
| 03 시 | 03:30 | 0330 | 03:45 | 3\~4시 | 4\~5시 | 5\~6시 | 6\~7시 | 7\~8시 | 8\~9시 |
| 04 시 | 04:30 | 0430 | 04:45 | 4\~5시 | 5\~6시 | 6\~7시 | 7\~8시 | 8\~9시 | 9\~10시 |
| 05 시 | 05:30 | 0530 | 05:45 | 5\~6시 | 6\~7시 | 7\~8시 | 8\~9시 | 9\~10시 | 10\~11시 |
| 06 시 | 06:30 | 0630 | 06:45 | 6\~7시 | 7\~8시 | 8\~9시 | 9\~10시 | 10\~11시 | 11\~12시 |
| 07 시 | 07:30 | 0730 | 07:45 | 7\~8시 | 8\~9시 | 9\~10시 | 10\~11시 | 11\~12시 | 12\~13시 |
| 08 시 | 08:30 | 0830 | 08:45 | 8\~9시 | 9\~10시 | 10\~11시 | 11\~12시 | 12\~13시 | 13\~14시 |
| 09 시 | 09:30 | 0930 | 09:45 | 9\~10시 | 10\~11시 | 11\~12시 | 12\~13시 | 13\~14시 | 14\~15시 |
| 10 시 | 10:30 | 1030 | 10:45 | 10\~11시 | 11\~12시 | 12\~13시 | 13\~14시 | 14\~15시 | 15\~16시 |
| 11 시 | 11:30 | 1130 | 11:45 | 11\~12시 | 12\~13시 | 13\~14시 | 14\~15시 | 15\~16시\~ | 16\~17시 |
| 12 시 | 12:30 | 1230 | 12:45 | 12\~13시 | 13\~14시 | 14\~15시 | 15\~16시 | 16\~17시 | 17\~18시 |
| 13 시 | 13:30 | 1330 | 13:45 | 13\~14시 | 14\~15시 | 15\~16시 | 16\~17시 | 17\~18시 | 18\~19시 |
| 14 시 | 14:30 | 1430 | 14:45 | 14\~15시 | 15\~16시 | 16\~17시 | 17\~18시 | 18\~19시 | 19\~20시 |
| 15 시 | 15:30 | 1530 | 15:45 | 15\~16시 | 16\~17시 | 17\~18시 | 18\~19시 | 19\~20시 | 20\~21시 |
| 16 시 | 16:30 | 1630 | 16:45 | 16\~17시 | 17\~18시 | 18\~19시 | 19\~20시 | 20\~21시 | 21\~22시 |
| 17 시 | 17:30 | 1730 | 17:45 | 17\~18시 | 18\~19시 | 19\~20시 | 20\~21시 | 21\~22시 | 22\~23시 |
| 18 시 | 18:30 | 1830 | 18:45 | 18\~19시 | 19\~20시 | 20\~21시 | 21\~22시 | 22\~23시 | 23\~24시 |
| 19 시 | 19:30 | 19030 | 19:45 | 19\~20시 | 20\~21시 | 21\~22시 | 22\~23시 | 23\~24시 | 24\~1시 |
| 20 시 | 20:30 | 2030 | 20:45 | 20\~21시 | 21\~22시 | 22\~23시 | 23\~24시 | 22\~23시 | 1\~2시 |
| 21 시 | 21:30 | 2130 | 21:45 | 21\~22시 | 22\~23시 | 23\~24시 | 0\~1시 | 1\~2시 | 2\~3시 |
| 22 시 | 22:30 | 2230 | 22:45 | 22\~23시 | 23\~24시 | 0\~1시 | 1\~2시 | 2\~3시 | 3\~4시 |
| 23 시 | 23:30 | 2330 | 23:45 | 23\~24시 | 0\~1시 | 1\~2시 | 2\~3시 | 3\~4시 | 4\~5시 |

❍ 최고/최저기온의 발표시간별 저장되는 예보자료 시간

| 발표시각 (KST) | 최저기온 |  |  |  |  | 최고기온 |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 오늘 | 내일 | 모레 | 글피 | 그글피 | 오늘 | 내일 | 모레 | 글피 | 그글피 |
| 2 | ○ | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |  |
| 5 |  | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |  |
| 8 |  | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |  |
| 11 |  | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |  |
| 14 |  | ○ | ○ | ○ |  |  | ○ | ○ | ○ |  |
| 17 |  | ○ | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |
| 20 |  | ○ | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |
| 23 |  | ○ | ○ | ○ | ○ |  | ○ | ○ | ○ | ○ |

**\# 예보요소 규칙**  
○ 하늘상태 : 상태변화 없음  
\- 하늘상태 단위

| 하늘상태 | 전운량 |
| :---: | :---: |
| 맑음 | 0 ～ 5 |
| 구름많음 | 6 ～ 8 |
| 흐림 | 9 ～ 10 |

○ 풍향  
\- 풍향 구간별 표현단위

| 풍향 구간(°) | 표현 단위 | 풍향 구간(°) | 표현 단위 |
| :---: | :---: | :---: | :---: |
| 0 – 45 | N-NE | 180 – 225 | S-SW |
| 45 – 90 | NE-E | 225 – 270 | SW-W |
| 90 – 135 | E-SE | 270 – 315 | W-NW |
| 135 – 180 | SE-S | 315 – 360 | NW-N |

○ 풍속  
\- 기상청 통보문의 육상예보에 사용하는 바람강도 용어  
![][image1]

**\# 풍향값에 따른 16방위 변환식**  
(풍향값 \+ 22.5 \* 0.5) / 22.5) \= 변환값(소수점 이하 버림)

| 변환값 | 16방위 |
| :---- | :---- |
| 0 | N |
| 1 | NNE |
| 2 | NE |
| 3 | ENE |
| 4 | E |
| 5 | ESE |
| 6 | SE |
| 7 | SSE |
| 8 | S |
| 9 | SSW |
| 10 | SW |
| 11 | WSW |
| 12 | W |
| 13 | WNW |
| 14 | NW |
| 15 | NNW |
| 16 | N |

예)  
풍향값 : 339  
변환값 : (339 \+ 22.5 \* 0.5 ) / 22.5 \= 15.5666... \=\> 15  
16방위 : NNW

풍향값 : 165  
변환값 : (165 \+ 22.5 \* 0.5 ) / 22.5 \= 7.8333... \=\> 7  
16방위 : SSE

**\#  단기예보 지점 좌표(X,Y)위치와 위경도 간의 전환 C 프로그램 예제**

\*\* 아래 프로그램은 위경도 값을 직접 좌표 값으로 변환하여 사용하기 원하는 사용자를 위한   
예제입니다.   
\*\* 행정구역별 지점 좌표(X,Y) 값은 별첨 엑셀 파일에 작성되어 제공 중입니다.   
\*\* 단기예보서비스는 남한에 대해서만 제공되며, 북한 및 국외는 제공되지 않습니다.  
\*\* 아래의 컴파일 방법은 예시이며, 사용하는 컴파일러나 툴 등에 맞춰 컴파일하면 됩니다.

○ 컴파일 방법 예시

\# cc 소스파일명 \-lm

○ 실행 방법 예시

\# 실행파일명 1 \<X-grid\> \<Y-grid\>  
예) \# a.out 1 59 125  
출력결과)X \= 59, Y \= 125 \---\>lon.= 126.929810, lat.= 37.488201

\# 실행파일명 0 \<경도\> \<위도\>  
예) \# a.out 0 126.929810 37.488201  
출력결과)lon.= 126.929810, lat.= 37.488201 \---\> X \= 59, Y \= 125

○ 소스파일

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<string.h\>  
\#include \<signal.h\>  
\#include \<sys/types.h\>  
\#include \<sys/stat.h\>  
\#include \<dirent.h\>  
\#include \<time.h\>  
\#include \<math.h\>

\#define NX 149 /\* X축 격자점 수 \*/  
\#define NY 253 /\* Y축 격자점 수 \*/

struct lamc\_parameter {  
	float Re; /\* 사용할 지구반경 \[ km \] \*/  
	float grid; /\* 격자간격 \[ km \] \*/  
	float slat1; /\* 표준위도 \[degree\] \*/  
	float slat2; /\* 표준위도 \[degree\] \*/  
	float olon; /\* 기준점의 경도 \[degree\] \*/  
	float olat; /\* 기준점의 위도 \[degree\] \*/  
	float xo; /\* 기준점의 X좌표 \[격자거리\] \*/  
	float yo; /\* 기준점의 Y좌표 \[격자거리\] \*/  
	int first; /\* 시작여부 (0 \= 시작) \*/  
};

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*  
\* MAIN  
\*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/  
int main (int argc, char \*argv\[\]) {  
	float lon, lat, x, y;  
	struct lamc\_parameter map;

	//  
	// 인수 확인  
	//

	if (argc \!= 4\) {  
		printf("\[Usage\] %s 1 \<X-grid\>\<Y-grid\>\\n", argv\[0\]);  
		printf(" %s 0 \<longitude\>\<latitude\>\\n", argv\[0\]);  
		exit(0);  
	}

	if (atoi(argv\[1\]) \== 1\) {  
		x \= atof(argv\[2\]);  
		y \= atof(argv\[3\]);

		if (x \< 1 || x \> NX || y \< 1 || y \> NY) {  
			printf("X-grid range \[1,%d\] / Y-grid range \[1,%d\]\\n", NX, NY);  
			exit(0);  
		}  
	} else if (atoi(argv\[1\]) \== 0\) {  
		lon \= atof(argv\[2\]);  
		lat \= atof(argv\[3\]);  
	}

	//  
	// 단기예보 지도 정보  
	//

	map.Re \= 6371.00877; // 지도반경  
	map.grid \= 5.0; // 격자간격 (km)  
	map.slat1 \= 30.0; // 표준위도 1  
	map.slat2 \= 60.0; // 표준위도 2  
	map.olon \= 126.0; // 기준점 경도  
	map.olat \= 38.0; // 기준점 위도  
	map.xo \= 210/map.grid; // 기준점 X좌표  
	map.yo \= 675/map.grid; // 기준점 Y좌표  
	map.first \= 0;

	//  
	// 단기예보  
	//

	map\_conv(\&lon, \&lat, \&x, \&y, atoi(argv\[1\]), map);

	if (atoi(argv\[1\]))  
		printf("X \= %d, Y \= %d \---\>lon.= %f, lat.= %f\\n", (int)x, (int)y, lon, lat);  
	else  
		printf("lon.= %f, lat.= %f \---\> X \= %d, Y \= %d\\n", lon, lat, (int)x, (int)y);

	return 0;  
}

/\*============================================================================\*  
\* 좌표변환  
\*============================================================================\*/  
int map\_conv  
(  
float \*lon, // 경도(degree)  
float \*lat, // 위도(degree)  
float \*x, // X격자 (grid)  
float \*y, // Y격자 (grid)  
int code, // 0 (격자-\>위경도), 1 (위경도-\>격자)  
struct lamc\_parameter map // 지도정보  
) {  
	float lon1, lat1, x1, y1;

	//  
	// 위경도 \-\> (X,Y)  
	//

	if (code \== 0\) {  
		lon1 \= \*lon;  
		lat1 \= \*lat;  
		lamcproj(\&lon1, \&lat1, \&x1, \&y1, 0, \&map);  
		\*x \= (int)(x1 \+ 1.5);  
		\*y \= (int)(y1 \+ 1.5);  
	}

	//  
	// (X,Y) \-\> 위경도  
	//

	if (code \== 1\) {  
		x1 \= \*x \- 1;  
		y1 \= \*y \- 1;  
		lamcproj(\&lon1, \&lat1, \&x1, \&y1, 1, \&map);  
		\*lon \= lon1;  
		\*lat \= lat1;  
	}  
	return 0;  
}

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*  
\* \[ Lambert Conformal Conic Projection \]  
\*  
\* olon, lat : (longitude,latitude) at earth \[degree\]  
\* o x, y : (x,y) cordinate in map \[grid\]  
\* o code \= 0 : (lon,lat) \--\> (x,y)  
\* 1 : (x,y) \--\> (lon,lat)  
\*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

int lamcproj(lon, lat, x, y, code, map)

float \*lon, \*lat; /\* Longitude, Latitude \[degree\] \*/  
float \*x, \*y; /\* Coordinate in Map \[grid\] \*/  
int code; /\* (0) lon,lat \-\>x,y (1) x,y \-\>lon,lat \*/  
struct lamc\_parameter \*map;  
{  
	static double PI, DEGRAD, RADDEG;  
	static double re, olon, olat, sn, sf, ro;  
	double slat1, slat2, alon, alat, xn, yn, ra, theta;

	if ((\*map).first \== 0\) {  
		PI \= asin(1.0)\*2.0;  
		DEGRAD \= PI/180.0;  
		RADDEG \= 180.0/PI;

		re \= (\*map).Re/(\*map).grid;  
		slat1 \= (\*map).slat1 \* DEGRAD;  
		slat2 \= (\*map).slat2 \* DEGRAD;  
		olon \= (\*map).olon \* DEGRAD;  
		olat \= (\*map).olat \* DEGRAD;

		sn \= tan(PI\*0.25 \+ slat2\*0.5)/tan(PI\*0.25 \+ slat1\*0.5);  
		sn \= log(cos(slat1)/cos(slat2))/log(sn);  
		sf \= tan(PI\*0.25 \+ slat1\*0.5);  
		sf \= pow(sf,sn)\*cos(slat1)/sn;  
		ro \= tan(PI\*0.25 \+ olat\*0.5);  
		ro \= re\*sf/pow(ro,sn);  
		(\*map).first \= 1;  
	}

	if (code \== 0\) {  
		ra \= tan(PI\*0.25+(\*lat)\*DEGRAD\*0.5);  
		ra \= re\*sf/pow(ra,sn);  
		theta \= (\*lon)\*DEGRAD \- olon;  
		if (theta \> PI) theta \-= 2.0\*PI;  
		if (theta \< \-PI) theta \+= 2.0\*PI;  
		theta \*= sn;  
		\*x \= (float)(ra\*sin(theta)) \+ (\*map).xo;  
		\*y \= (float)(ro \- ra\*cos(theta)) \+ (\*map).yo;  
	} else {  
		xn \= \*x \- (\*map).xo;  
		yn \= ro \- \*y \+ (\*map).yo;  
		ra \= sqrt(xn\*xn+yn\*yn);  
		if (sn\< 0.0) \-ra;  
		alat \= pow((re\*sf/ra),(1.0/sn));  
		alat \= 2.0\*atan(alat) \- PI\*0.5;  
		if (fabs(xn) \<= 0.0) {  
			theta \= 0.0;  
		} else {  
			if (fabs(yn) \<= 0.0) {  
				theta \= PI\*0.5;  
				if(xn\< 0.0 ) \-theta;  
			} else  
				theta \= atan2(xn,yn);  
		}  
		alon \= theta/sn \+ olon;  
		\*lat \= (float)(alat\*RADDEG);  
		\*lon \= (float)(alon\*RADDEG);  
	}  
	return 0;  
}  
※ Open API 에러 코드 정리

| 에러코드 | 에러메세지 | 설명 |
| :---: | ----- | ----- |
| 00 | NORMAL\_SERVICE | 정상 |
| 01 | APPLICATION\_ERROR | 어플리케이션 에러 |
| 02 | DB\_ERROR | 데이터베이스 에러 |
| 03 | NODATA\_ERROR | 데이터없음 에러 |
| 04 | HTTP\_ERROR | HTTP 에러 |
| 05 | SERVICETIME\_OUT | 서비스 연결실패 에러 |
| 10 | INVALID\_REQUEST\_PARAMETER\_ERROR | 잘못된 요청 파라메터 에러 |
| 11 | NO\_MANDATORY\_REQUEST\_PARAMETERS\_ERROR | 필수요청 파라메터가 없음 |
| 12 | NO\_OPENAPI\_SERVICE\_ERROR | 해당 오픈API서비스가 없거나 폐기됨 |
| 20 | SERVICE\_ACCESS\_DENIED\_ERROR | 서비스 접근거부 |
| 21 | TEMPORARILY\_DISABLE\_THE\_SERVICEKEY\_ERROR | 일시적으로 사용할 수 없는 서비스 키 |
| 22 | LIMITED\_NUMBER\_OF\_SERVICE\_REQUESTS\_EXCEEDS\_ERROR | 서비스 요청제한횟수 초과에러 |
| 30 | SERVICE\_KEY\_IS\_NOT\_REGISTERED\_ERROR | 등록되지 않은 서비스키 |
| 31 | DEADLINE\_HAS\_EXPIRED\_ERROR | 기한만료된 서비스키 |
| 32 | UNREGISTERED\_IP\_ERROR | 등록되지 않은 IP |
| 33 | UNSIGNED\_CALL\_ERROR | 서명되지 않은 호출 |
| 99 | UNKNOWN\_ERROR | 기타에러 |

[image1]: <data:image/png;base64,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>