from urllib.parse import quote
import requests
def info(id):
    header = {'laftel': 'TeJava'}

    laftel_API = 'https://laftel.net/api/items/v2/' + str(id)
    response = requests.get(url=laftel_API, headers=header)

    results = response.json()

    result = [id, results["name"], results["content"], results["images"][0]["img_url"], results["air_year_quarter"], results["content_rating"], results["avg_rating"], results["production"], results["genres"]]

    return result