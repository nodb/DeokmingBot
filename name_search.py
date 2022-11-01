from urllib.parse import quote
import requests

name = input()  # 이름 입력
encoding = quote(name)

header = {'laftel': 'TeJava'}

laftel_API = 'https://laftel.net/api/search/v1/keyword/?keyword={' + str(encoding) + '}'
response = requests.get(url = laftel_API, headers = header)

json = response.json()
results = json["results"]

# 전체 출력
# print(response.text)

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

# 제목
# 평점
# 장르
# 연령제한
# 개요
# 제작사
# 출시