from urllib.parse import quote
import requests
def quarter(date):
    encoding = quote(date)
    header = {'laftel': 'TeJava'}

    laftel_API = 'https://laftel.net/api/search/v1/discover/?years=' + str(encoding)

    result = []

    while (True):
        response = requests.get(url=laftel_API, headers=header)
        json = response.json()
        results = json["results"]


        for i, x in enumerate(results, 1):
            result.append({'name': x["name"], 'id': x["id"]})

        next = json["next"]
        if (next is not None):
            laftel_API = next
        else:
            break
        # time.sleep(random.randint(1, 2))

    return result