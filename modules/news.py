import requests
import os

newsapi = os.getenv("NEWS_API_KEY")

def get_news():

    r = requests.get(
        f"https://newsapi.org/v2/everything?q=tesla&from=2026-04-12&sortBy=publishedAt&apiKey={newsapi}"
    )

    if r.status_code == 200:

        data = r.json()

        return data["articles"][:5]

    return []