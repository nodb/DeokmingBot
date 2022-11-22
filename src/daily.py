import requests
from bs4 import BeautifulSoup
from datetime import datetime

def daily(day):
  header = {'laftel': 'TeJava'}

  laftel_API = 'https://laftel.net/daily'
  response = requests.get(url = laftel_API, headers = header)
  response.encoding = None

  soup = BeautifulSoup(response.text, "lxml")

  if day=="오늘":
    today = datetime.today().weekday()
    day = {0: "월요일", 1: "화요일", 2: "수요일", 3: "목요일", 4: "금요일", 5: "토요일", 6: "일요일"}.get(today)

  results = soup.find("h3", text=day).next_siblings

  result = []
  for i, x in enumerate(results, 1):
    name = x.get_text()
    if name.strip()[-2]=='U' and name.strip()[-1]=='P':
      name = name[:-2]
    id = x["href"]
    id = id[6:11]
    result.append({'name': name, 'id': id})

  return result