from django.core.cache import cache

def fetch_country():
    "Fetch lists of countries in Middleware code"
    return cache.get('remote_countries')