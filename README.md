# Fint Server API

원티드 프리온보딩 백엔드 기업 과제

## 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [과제 요구사항 분석](#과제-요구사항-분석)
3. [프로젝트 기술 스택](#프로젝트-기술-스택)
4. [개발 기간](#개발-기간)
5. [팀 구성](#팀-구성)
6. [역할](#역할)
7. [ERD](#ERD)
8. [API 목록](#API-목록)
9. [프로젝트 시작 방법](#프로젝트-시작-방법)

<br>

## 프로젝트 개요

고객 투자 데이터를 제공하는 Django 기반 API 서버입니다.

<br>

## 과제 요구사항 분석

### 1. 배치 스크립트 작성

- APScheduler 사용
- 매일 자정에 스크립트가 실행되도록 설정

### 2. 데이터 조회 API

- 투자 화면
    - 사용자명
    - 계좌명
    - 증권사
    - 계좌번호
    - 계좌 총 자산 (보유 종목들의 평가 금액 총합)
- 투자상세 화면
    - 계좌명
    - 증권사
    - 계좌번호
    - 계좌 총 자산
    - 투자 원금
    - 총 수익금 (총 자산 - 투자 원금)
    - 수익률 (총 수익금 / 투자 원금 * 100)
- 보유종목 화면
    - 보유 종목명
    - 보유 종목의 자산군
    - 보유 종목의 평가 금액(종목 보유 수량 * 종목 현재가)
    - 보유 종목 ISIN

### 3. 투자금 입금 API

- Phase 1 : 거래 정보 등록
    - 요청 데이터
        - 계좌번호
        - 고객명
        - 거래 금액
    - 응답 데이터
        - 거래정보 식별자
- Phase 2 : phase1 에서 등록한 거래정보 검증 후 실제 고객의 자산을 업데이트
    - 요청 데이터
        - phase1 요청 데이터 계좌번호, 고객명, 거래 금액 순서로 연결한 string 을 hash한 string
            - hashlib 라이브러리를 사용해 SHA256으로 암호화
        - phase1 에서 응답받은 거래정보 식별자
    - 응답 데이터
        - 입금 거래 결과
    - 수행 작업
        - 입금 내역 상태 변경
        - 투자 원금 업데이트
        - 현금 자산 업데이트

<br>

## 프로젝트 기술 스택

### Backend

<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB

<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools

<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-5865F2?logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
</section>

<br>

## 개발 기간

- 2022/09/16~2022/09/21

<br>

## 팀 구성

개인 프로젝트

<br>

## 역할

1. 요구사항 분석
2. 모델 및 API 설계
3. API 구현
4. 프로젝트 문서 작성

<br>

## ERD

![](https://i.imgur.com/CADbmHg.png)

<br>

## API 목록

https://app.swaggerhub.com/apis/BomiChoi/fint-server-api/v1

## 프로젝트 시작 방법

1. 로컬에서 실행할 경우

```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch ${github 주소}
cd ${디렉터리 명}

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>
