import requests

def fetch(url: str) -> list:
    try:
        response = requests.get(url)
        data = response.text

        return data
    except:
        return []