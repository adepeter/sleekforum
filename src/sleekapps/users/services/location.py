import requests

def fetch_country():
    api_url = 'https://restcountries.eu/rest/v2/all'
    return requests.get(api_url)