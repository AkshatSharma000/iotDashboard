import requests

def api_info():
    url = 'http://127.0.0.1:8000/'
    r = requests.get(url)
    data = r.json()

    return data
