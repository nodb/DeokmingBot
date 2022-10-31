import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://laftel.net/daily")
page.raise_for_status()		# 페이지 못 불러올 경우 종료

# soup = bs(page.text, "html.parser")
# elements = soup.select('a.daily-item > div > div')
#
# for index, element in enumerate(elements, 1):
# 	print("{} 번째 게시글의 제목: {}".format(index, element.text))

print(len(page.text))

with open("laftel.html", "w", encoding="utf8") as f:
	f.write(page.text)