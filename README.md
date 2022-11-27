# 디스코드 애니메이션 추천 봇👾 </br> 덕밍아웃 | DeokmingBot🦾
<img alt = "덕밍아웃로고" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/logo.png" width="300">

## ✍ Project Introduction
*"애니메이션 사이트를 항상 띄워두진 않지만, 많은 사람들이 디스코드는 시작프로그램으로 상시 사용한다. 그렇다면 디스코드를 통해 원하는 애니메이션에 대한 정보 빠르게 찾을수 있다면 어떨까?"*

**"덕밍봇"** 은 **Discord Bot API** 를 이용한 디스코드 서버 유틸리티 봇으로  디스코드 명령만으로 애니메이션을 즐겨보는 유저를 위한 검색, 추천 등 다양한 편리한 기능을 제공합니다.

## 🗂️ Project Structure
프로젝트 DeokmingBot의 'main' branch 디렉토리 구조입니다.

**📁 /resources**
```
🎨 command_*.jpg
명령어 수행 이미지

🎨 logo.png
덕밍아웃 로고 이미지
```
**📁 /src**
```
📄 daily.py
라프텔의 요일별 신작 페이지를 이용해 요일별 작품 '제목'을 스크래핑하는 파일

📄 genre.py
라프텔의 discover API에 '선택 장르' 및 '제외 장르' key를 원하는 value를 적용해 순위별 작품 '제목', 'id'를 스크래핑하는 파일

📄 info.py
라프텔의 작품 API에 원하는 'id'를 value로 적용해 해당 'id'의 작품 '제목', '내용', '출시', '이용등급', '평점', '제작사', '장르'를 스크래핑하는 파일

📄 main.py
discord bot 활성화 파일, 명령어 정의 및 최종 실행 파일

📄 name.py
라프텔의 키워드 API에 원하는 '제목'을 value로 적용해 해당 '제목'의 작품 'id'를 스크래핑하여 'info.py'로 값을 넘기는 파일

📄 quarter.py
라프텔의 discover API에 'year key'를 원하는 '년', '분기' value를 적용해 순위별 작품 '제목', 'id'를 스크래핑하는 파일

📄 rank.py
라프텔의 recommend API에 'ranking type' key를 원하는 value를 적용해 순위별 작품 '제목', 'id'를 스크래핑하는 파일

📄 top10.py
네이버 실시간 검색어의 API에 순위별 검색어 'keyword'를 스크래핑하는 파일
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

## 📦 Package
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

## 📜 Command

**덕밍아웃 봇**은 슬래시 명령어(**/명령내용**) 방법을 사용합니다.  
**덕밍아웃 봇**은 다음과 같은 기능을 제공합니다.

✨ 서버에 새로운 멤버가 입장하거나 퇴장 시에 환영 문구 또는 퇴장 알림 메세지를 출력합니다.

📝 /명령어
```
수행 가능한 명령어들을 조회할 수 있습니다.
```
✅ /명령어  
<img alt = "명령어1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EB%AA%85%EB%A0%B9%EC%96%B41.jpg" width="725">
<img alt = "명령어2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EB%AA%85%EB%A0%B9%EC%96%B42.jpg" width="725">

🔍 /애니 [작품]
```
'/애니'를 입력하고 원하는 '작품'을 입력하면 해당 작품의 정보를 출력합니다.
작품에 대한 간단한 개요와 세부 내용 및 시청할 수 있는 링크를 제공합니다.
만약 작품명이 잘못 입력한 경우 채팅방에 오류 알림 메세지를 반환합니다.
```
✅ /애니 스파이패밀리  
<img alt = "애니1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%95%A0%EB%8B%881.jpg" width="725">
<img alt = "애니2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%95%A0%EB%8B%882.jpg" width="725">


🔍 /장르 [장르1] [장르2]..
```
'/장르'를 입력하면 장르 옵션
'개그|공포|드라마|로맨스|모험|무협|미스터리|범죄|스릴러|스포츠|시대물|아동|아이돌|액션|음식|음악|이세계|일상|재난|추리|치유|특촬|판타지'
이 생성되고 장르를 선택하려면 '+', 제외하려면 '-'를 입력하면 조건을 만족하는 추천 작품들을 출력합니다.
```
✅ /장르 [개그]+ [액션]+ [판타지]-  
<img alt = "장르1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%9E%A5%EB%A5%B41.jpg" width="725">
<img alt = "장르2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%9E%A5%EB%A5%B42.jpg" width="725">
<img alt = "장르3" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%9E%A5%EB%A5%B43.jpg" width="725">

🔍 /인기 [기간]
```
'/인기'를 입력하면 기간 옵션 '실시간|이번주|분기|역대'이 생성되고
기간 선택시 해당 기간의 인기 작품들을 출력합니다.
```
✅ /인기 이번주  
<img alt = "인기1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%9D%B8%EA%B8%B01.jpg" width="725">
<img alt = "인기2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%9D%B8%EA%B8%B02.jpg" width="725">

🔍 /신작 [요일]
```
'/신작'을 입력하면 요일 옵션 '오늘|월요일|화요일|수요일|목요일|금요일|토요일|일요일'이 생성되고
요일 선택시 해당 요일의 현재 방영중인 신작을 출력합니다.
```
✅ /신작 월요일  
<img alt = "신작1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%8B%A0%EC%9E%911.jpg" width="725">
<img alt = "신작2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%8B%A0%EC%9E%912.jpg" width="725">

🔍 /분기 [년도] [분기]
```
'/분기'를 입력하면 년도 옵션 '1918~올해'과 분기 옵션 '1|2|3|4'이 생성되고
선택시 해당 년도의 분기에 방영했던 모든 작품들을 인기순으로 출력합니다.
만약 년도를 잘못 입력할 경우 채팅방에 오류 알림 메세지를 반환합니다.
```
✅ /분기 2022 3  
<img alt = "분기1" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EB%B6%84%EA%B8%B01.jpg" width="725">
<img alt = "분기2" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EB%B6%84%EA%B8%B02.jpg" width="725">

✨ 그 외 소소한 기능으로 네이버 실시간 인기 검색어 순위를 확인하는 `/실검` 명령어, 디스코드 봇의 지연율을 확인하는 `/지연` 명령어, 제작자를 확인하는 `/제작` 명령어가 있습니다.  
✅ /실검  
<img alt = "실검" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%8B%A4%EA%B2%80.jpg" width="725">
✅ /지연  
<img alt = "지연" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%A7%80%EC%97%B0.jpg" width="725">
✅ /제작
<img alt = "제작" src="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/command_%EC%A0%9C%EC%9E%91.jpg" width="725">

## 📚️ Deployment

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
덕밍아웃 봇은 [replit](https://replit.com/@nodb/DeokmingBot#main.py), [uptimerobot](https://uptimerobot.com/)을 이용하여 배포되며 상시 작동 중입니다. 
- [replit](https://replit.com/@nodb/DeokmingBot#main.py) : 프로젝트 생성(웹 프레임워크로 사이트 제작)
- [uptimerobot](https://uptimerobot.com/) : 호스팅 유지(웹 사이트 주기적 접근)


## 🔗 Reference
- [Discord Developer Portal](https://discord.com/developers/docs/intro) - 디스코드 공식 API 참고
- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) - discord.py 명령어 참고
- [Civo | youtube | How to make Your First Discord Bot](https://www.youtube.com/watch?v=2u9a9WmlQro&ab_channel=Civo) - discord.py 명령어 참고
- [가비아 라이브러리 | BeautifulSoup와 requests로 웹 파싱해보기](https://library.gabia.com/contents/9239/) - 파이썬 웹 스크래핑 참고
- [나도코딩 | youtube | 웹 크롤링? 웹 스크래핑!](https://www.youtube.com/watch?v=yQ20jZwDjTE&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9) - 파이썬 웹 스크래핑 참고
- [zetbouaka | velog | 라프텔 API](https://velog.io/@zetbouaka/series/%EB%9D%BC%ED%94%84%ED%85%94-API%EB%B9%84%EA%B3%B5%EC%8B%9D) - 라프텔 API 참고
- [코코블루 | 네이버블로그 | 디스코드 서버](https://blog.naver.com/PostView.naver?blogId=6116949&logNo=221949748751&redirect=Dlog&widgetTypeCall=true&directAccess=false) - 서버 입장/퇴장 사람 감지 코드 참고
- [Stack Overflow | discord.py error message](https://stackoverflow.com/questions/71177867/discord-py-error-message-this-interaction-failed) - 버튼 에러 코드 참고
- [이불색하늘 | 블로그 | Pycord](https://blog.chnrit.com/pycord-3-ephemeral-message/) - 비공개 상호작용 방법 참고
- [최신코딩 | youtube | repl.it 24시간 서버 구축](https://www.youtube.com/watch?v=qj_f1KDh6Gg&ab_channel=%EC%B5%9C%EC%8B%A0%EC%BD%94%EB%94%A9) - repl.it & uptimerobot 서버 호스팅 참고
- [뒬탕 | tistory | 리플릿 사용법 및 호스팅](https://programming4myself.tistory.com/4) - repl.it & uptimerobot 서버 호스팅 참고

## 🧑‍💻 Developer

| 학과         | 학번     | 이름   |
| ------------ | -------- | ------ |
| 컴퓨터공학과 | 19101216 | 노다빈 |

## 💳 License

이 프로젝트는 MIT 라이선스로 배포됩니다.  
상세한 라이선스 정보는 [LICENSE](https://github.com/nodb/DeokmingBot/blob/main/LICENSE) 파일에서 확인할 수 있습니다.