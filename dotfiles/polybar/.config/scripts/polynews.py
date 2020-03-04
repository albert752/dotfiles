#!/usr/bin/python

import requests
from pprint import pprint as pp
#get your api key at https://newsapi.org/

api_key = "0677e692bd974044a9ff4e3ba79269eb"

#find sources & country codes at https://newsapi.org/sources

sources = "news24"
country = ""

try:
    data = requests.get('https://newsapi.org/v2/top-headlines?apiKey='+api_key+'&sources='+sources+'&country='+country).json()
    pp(data)
    sourceName = data['articles'][0]['source']['name']
    title = data['articles'][0]['title']
    url = data['articles'][0]['url']
    print(sourceName+': '+title)
 
except requests.exceptions.RequestException as e:
    print ('Something went wrong!')

