import requests

from django.core.cache import cache

def fetch_country():
    api_url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(api_url)
    if cache.has_key('api_countries_fetch'):
        return cache.get('api_countries_fetch')
    else:
        if response.status_code == 200:
            countries = response.json()
            return cache.set('api_countries_fetch', countries, None)