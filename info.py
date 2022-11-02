from urllib.parse import quote
import requests

id = input()  # 작품 id 입력
encoding = quote(id)

header = {'laftel': 'TeJava'}

laftel_API = 'https://laftel.net/api/items/v2/' + str(encoding)
response = requests.get(url = laftel_API, headers = header)

result = response.json()

# 전체 출력
# print(response.text)

# 목록 출력
# for x in results:
#   print(x["name"])

# 정보 출력
print(result["id"])                   # id
print(result["name"])                 # 제목
print(result["img"])                  # 메인 사진
print(result["images"][0]["img_url"])   # 원본 메인 사진
if(len(result["images"])==2):
  print(result["images"][1]["img_url"]) # 원본 배경 사진
print(result["content"])              # 내용 개요
print(result["content_rating"])       # 이용가
print(result["production"])           # 분기
print(result["distributed_air_time"]) # 요일
print(result["genres"])               # 장르
print(result["avg_rating"])           # 평점
print(result["tags"])                 # 태그
print(result["series_id"])            # 시리즈 id
print("https://laftel.net/item/" + str(result["id"]))  # url



# 제목
# 평점
# 장르
# 연령제한
# 개요
# 제작사
# 출시