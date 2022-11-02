from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

# day = input()  # 이름 입력
# encoding = quote(day)

header = {'laftel': 'TeJava'}

laftel_API = 'https://laftel.net/daily'
response = requests.get(url = laftel_API, headers = header)
response.encoding = None

soup = BeautifulSoup(response.text, "lxml")

for day in ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]:
    results = soup.find("h3", text=day).next_siblings
    print(day)
    for x in results:
        print(x.get_text())     # 이름
        print("https://laftel.net" + quote(x["href"]))  # url
    print('\n')