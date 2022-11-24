# 디스코드 애니메이션 추천 봇 </br> 덕밍아웃 | DeokmingBot
<img alt = "덕밍아웃로고" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/logo.png" width="300">

### ✍ Project Introduction
*"애니메이션 사이트를 항상 띄워두진 않지만, 많은 사람들이 디스코드는 시작프로그램으로 상시 사용한다. 그렇다면 디스코드를 통해 원하는 애니메이션에 대한 정보 빠르게 찾을수 있다면 어떨까?"*

**"덕밍봇"** 은 **Discord Bot API** 를 이용한 디스코드 서버 유틸리티 봇으로  디스코드 명령만으로 애니메이션을 즐겨보는 유저를 위한 검색, 추천 등 다양한 편리한 기능을 제공합니다.

### 🗂️ Project Structure
프로젝트 DeokmingBot의 'main' branch 디렉토리 구조입니다.

**📁 /resources**
```
🎨 command_*.png
명령어 수행 이미지

🎨 logo.png
덕밍아웃 로고 이미지
```
**📁 /src**
```
📄 daily.py
라프텔의 요일별 신작 페이지를 이용해 요일별 작품 '제목'을 크롤링하는 파일

📄 genre.py
라프텔의 discover API에 '선택 장르' 및 '제외 장르' key를 원하는 value를 적용해 순위별 작품 '제목', 'id'를 크롤링하는 파일

📄 info.py
라프텔의 작품 API에 원하는 'id'를 value로 적용해 해당 'id'의 작품 '제목', '내용', '출시', '이용등급', '평점', '제작사', '장르'를 크롤링하는 파일

📄 main.py
discord bot 활성화 파일, 명령어 정의 및 최종 실행 파일

📄 name.py
라프텔의 키워드 API에 원하는 '제목'을 value로 적용해 해당 '제목'의 작품 'id'를 크롤링하여 'info.py'로 값을 넘기는 파일

📄 quarter.py
라프텔의 discover API에 'year key'를 원하는 '년', '분기' value를 적용해 순위별 작품 '제목', 'id'를 크롤링하는 파일

📄 rank.py
라프텔의 recommend API에 'ranking type' key를 원하는 value를 적용해 순위별 작품 '제목', 'id'를 크롤링하는 파일

📄 top10.py
네이버 실시간 검색어의 API에 순위별 검색어 'keyword'를 크롤링하는 파일
```

**📁 /**
```
📄 LICENSE
프로젝트 라이선스 파일
📄 README.md
프로젝트 설명 파일, 현 실행 파일
📄 requirement.txt
프로젝트 실행에 요구되는 패키지 모음 파일
```

### 📦 Package
이 프로젝트는 discord.py와 py-cord를 기반으로 개발되었습니다.  

개발에 사용된 패키지 목록  
📄 [requirement.txt](https://github.com/nodb/DeokmingBot/blob/main/requirement.txt)
```
discord
discord.py
py-cord
beautifulsoup4
lxml
requests
urllib3
```
pip install -r requirement.txt 명령어로 한번에 설치 가능합니다.

### 📜 Command

**덕밍아웃 봇**은 슬래시 명령어(**/명령내용**) 방법을 사용합니다.  
**덕밍아웃 봇**은 다음과 같은 기능을 제공합니다.

✨ 서버에 새로운 멤버가 입장하거나 퇴장 시에 환영 문구 또는 퇴장 알림 메세지를 출력합니다.

🔍 /명령어
```
수행 가능한 명령어들을 조회할 수 있습니다.
```
✅ /명령어

🔍 /애니 [작품]
```
'/애니'를 입력하고 원하는 '작품'을 입력하면 해당 작품의 정보를 출력합니다.
작품에 대한 간단한 개요와 세부 내용 및 시청할 수 있는 링크를 제공합니다.
만약 작품명이 잘못 입력한 경우 채팅방에 오류 알림 메세지를 반환합니다.
```
✅ /애니 스파이패밀리

🔍 /장르 [장르1] [장르2]..
```
'/장르'를 입력하면 장르 옵션
'개그|공포|드라마|로맨스|모험|무협|미스터리|범죄|스릴러|스포츠|시대물|아동|아이돌|액션|음식|음악|이세계|일상|재난|추리|치유|특촬|판타지'
이 생성되고 장르를 선택하려면 '+', 제외하려면 '-'를 입력하면 조건을 만족하는 추천 작품들을 출력합니다.
```
✅ /장르 [개그]+ [액션]+ [판타지]-

🔍 /인기 [기간]
```
'/인기'를 입력하면 기간 옵션 '실시간|이번주|분기|역대'이 생성되고
기간 선택시 해당 기간의 인기 작품들을 출력합니다.
```
✅ /인기 이번주

🔍 /신작 [요일]
```
'/신작'을 입력하면 요일 옵션 '오늘|월요일|화요일|수요일|목요일|금요일|토요일|일요일'이 생성되고
요일 선택시 해당 요일의 현재 방영중인 신작을 출력합니다.
```
✅ /신작 월요일

🔍 /분기 [년도] [분기]
```
'/분기'를 입력하면 년도 옵션 '1918~올해'과 분기 옵션 '1|2|3|4'이 생성되고
선택시 해당 년도의 분기에 방영했던 모든 작품들을 인기순으로 출력합니다.
만약 년도를 잘못 입력할 경우 채팅방에 오류 알림 메세지를 반환합니다.
```
✅ /분기 2022 3

✨ 그 외 소소한 기능으로 네이버 실시간 인기 검색어 순위를 확인하는 `/실검` 명령어, 디스코드 봇의 지연율을 확인하는 `/지연` 명령어, 제작자를 확인하는 `/제작` 명령어가 있습니다.  
✅ /실검  
✅ /지연  
✅ /제작

### 📚️ Deployment

**서버에 덕밍아웃 봇 추가하기**
1. [초대링크](https://discord.com/api/oauth2/authorize?client_id=1036483177805516851&permissions=8&scope=bot)를 클릭하여 접속합니다.
2. 디스코드에 로그인합니다.
3. 봇을 추가할 서버를 선택합니다.
    - 봇은 서버 주인만 초대할 수 있습니다.
4. 계속하기 버튼을 클릭합니다.
5. 관리자 권한을 체크하고 승인 버튼을 클릭합니다.
    - 관리자 권한을 허용해야 모든 기능을 사용할 수 있습니다.
---
**서버 호스팅**  
덕밍아웃 봇은 [replit](https://replit.com/), [uptimerobot](https://uptimerobot.com/)을 이용하여 배포되며 상시 작동 중입니다. 
- [replit](https://replit.com/) : 프로젝트 생성(웹 프레임워크로 사이트 제작)
- [uptimerobot](https://uptimerobot.com/) : 호스팅 유지(웹 사이트 주기적 접근)


### 🔗 Reference


### 🧑‍💻 Developer

| 학과         | 학번     | 이름   |
| ------------ | -------- | ------ |
| 컴퓨터공학과 | 19101216 | 노다빈 |

### 💳 License

이 프로젝트는 MIT 라이선스로 배포됩니다.  
상세한 라이선스 정보는 [LICENSE](https://github.com/nodb/DeokmingBot/blob/main/LICENSE) 파일에서 확인할 수 있습니다.