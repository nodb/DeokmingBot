# 디스코드 애니메이션 추천 봇 </br> 덕밍봇 | DeokmingBot

## 프로젝트 제작

| 학과         | 학번     | 이름   |
| ------------ | -------- | ------ |
| 컴퓨터공학과 | 19101216 | 노다빈 |

## 프로젝트 설명
*"애니메이션 사이트를 항상 띄워두진 않지만, 많은 사람들이 디스코드는 시작프로그램으로 상시 사용한다. 그렇다면 디스코드를 통해 원하는 애니메이션에 대한 정보 빠르게 찾을수 있다면 어떨까?"*

**"덕밍봇"** 은 **Discord Bot API** 를 이용한 디스코드 서버 유틸리티 봇으로  디스코드 명령만으로 애니메이션을 즐겨보는 유저를 위해 검색 기능, 추천 기능 등 다양한 편리한 기능을 제공합니다.

**덕밍봇**은 다음과 같은 기능을 제공합니다.
- 덕밍봇을 디스코드 서버에 초대하면 채팅방에 안내 메세지를 띄웁니다.
- 서버에 새로운 멤버가 입장하거나 퇴장 시에도 환영 문구 또는 퇴장 알림 메세지를 출력합니다.
- `/명령어` : 수행 가능한 명령어들을 조회할 수 있습니다.
- `/애니 [작품]` : `/애니`를 입력하고 원하는 `작품`을 입력하면 해당 작품의 정보를 디스코드 채팅방에 출력합니다. (예시: `/애니 명탐정코난`)
작품에 대한 간단한 개요와 세부 내용 및 시청할 수 있는 링크를 제공받을 수 있습니다.
만약 작품명이 잘못 입력한 경우 채팅방에 오류 알림 메세지를 반환합니다.
- `/장르 [장르1] [장르2]..` : `/장르`을 입력하면 `장르`옵션 `개그|공포|드라마|로맨스|모험|무협|미스터리|범죄|스릴러|스포츠|시대물|아동|아이돌|액션|음식|음악|이세계|일상|재난|추리|치유|특촬|판타지`이 생성되고 장르를 선택하려면 +, 제외하려면 -를 입력하여 조건을 만족하는 추천 작품들을 디스코드 채팅방에 출력합니다. (예시: `/장르 [추리]+ [개그]-`)
- `/인기 [기간]` : `/인기`를 입력하면 `기간`옵션 `실시간|이번주|분기|역대`이 생성되고 기간 선택시 해당 기간의 인기 작품들을 디스코드 채팅방에 출력합니다.
- `/신작 [요일]` : `/신작`을 입력하면 `요일`옵션 `오늘|월요일|화요일|수요일|목요일|금요일|토요일|일요일`이 생성되고 요일 선택시 해당 요일의 현재 방영중인 신작을 디스코드 채팅방에 출력합니다.
- `/분기 [년도] [분기]` : `/분기`를 입력하면 `년도`옵션 (1918~이번년도)과 `분기`옵션 `1|2|3|4`가 생성되고 선택시 해당 년도의 분기에 방영했던 모든 작품들을 인기순으로 디스코드 채팅방에 출력합니다. (예시: `/분기 2020 1`)
만약 년도를 잘못 입력할 경우 채팅방에 오류 알림 메세지를 반환합니다.
- 그 외 소소한 기능으로 네이버 실시간 인기 검색어 순위를 확인하는 `/실검` 명령어, 디스코드 봇의 지연율을 확인하는 `/지연` 명령어, 제작자를 확인하는 `/제작` 명령어가 있습니다.