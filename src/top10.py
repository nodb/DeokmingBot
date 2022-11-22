from urllib.parse import quote
import requests

def top10():
    top_API = 'https://api.signal.bz/news/realtime'
    response = requests.get(url=top_API)

    results = response.json()

    result = []

    for x in results["top10"]:
        encoding = quote(x["keyword"])
        result.append(f'[{x["keyword"]}](<https://search.naver.com/search.naver?where=news&sm=tab_jum&query={encoding}>)')

    return result