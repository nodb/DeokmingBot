from urllib.parse import quote
import requests
import info

def name(title):
    encoding = quote(title)

    header = {'laftel': 'TeJava'}

    laftel_API = 'https://laftel.net/api/search/v1/keyword/?keyword={' + str(encoding) + '}'
    response = requests.get(url=laftel_API, headers=header)

    json = response.json()
    results = json["results"]

    result = info.info(results[0]["id"])

    return result