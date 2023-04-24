#!/usr/bin/python3
import requests

# this code will get the data from the request
data = requests.get('https://intranet.alxswe.com/rltoken/7cr7aLYdaWAZWBKrBKS12A')

print(data)
