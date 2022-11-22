from urllib.parse import quote
import requests

def rank(term):
  encoding = quote(term)

# 4hour 실시간
# week 이번주
# quarter 분기
# history 역대

  header = {'laftel': 'TeJava'}

  laftel_API = 'https://laftel.net/api/home/v1/recommend/ranking/?type=' + str(encoding)
  response = requests.get(url = laftel_API, headers = header)

  results = response.json()

  result = []
  for i, x in enumerate(results, 1):
    result.append({'id': x["id"], 'name': x["name"]})
    if i==12:
      break

  return result