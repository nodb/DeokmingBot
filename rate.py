import requests
from bs4 import BeautifulSoup

url = "https://laftel.net/item/40971/review"
res = requests.get(url)
res.raise_for_status()			# 페이지 못 불러올 경우 종료
res.encoding=None

soup = BeautifulSoup(res.text, "lxml")

info = soup.find("div", attrs={"id":"item-modal"})
print(info.h3.parent.next_sibling.div.div.get_text())