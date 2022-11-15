from urllib.parse import quote
import requests

def genre(selection, exception):
    encoding_S = quote(selection)
    encoding_E = quote(exception)
    header = {'laftel': 'TeJava'}

    laftel_API = 'https://laftel.net/api/search/v1/discover/?genres=' + str(encoding_S) + '&exclude_genres=' + str(encoding_E)

    result = []

    response = requests.get(url=laftel_API, headers=header)
    json = response.json()
    results = json["results"]

    for i, x in enumerate(results, 1):
        result.append({'name': x["name"], 'id': x["id"]})
        if i == 15:
            break

    return result