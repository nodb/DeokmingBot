from urllib.parse import quote
import requests

rank = input()  # 이름 입력
encoding = quote(rank)
# 4hour 실시간
# week 이번주
# quarter 분기
# history 역대

header = {'laftel': 'TeJava'}

laftel_API = 'https://laftel.net/api/home/v1/recommend/ranking/?type=' + str(encoding)
response = requests.get(url = laftel_API, headers = header)

results = response.json()

# 전체 출력
# print(results)

# 목록 출력
# for x in results:
#   print(x["name"])

# 정보 출력
for x in results:
  print(x["id"])        # id
  print(x["name"])      # 제목
  print(x["img"])       # 메인 사진
  print(x["images"][0]["img_url"])  # 원본 메인 사진
  if(len(x["images"])==2):
    print(x["images"][1]["img_url"])  # 원본 배경 사진
  print(x["is_adult"])  # 성인용 여부
  print(x["genres"], '\n')    # 장르