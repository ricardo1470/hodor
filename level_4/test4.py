#!/usr/bin/python3
import requests
from colorama import Fore

url = 'http://158.69.76.135/level4.php'
myobj = {'id': '1466', 'holdthedoor': 'Submit'}

x = requests.post(url, data=myobj)
print(x.status_code)


r = requests.head(url, data={'key':'value'})
print(r.headers)
print(r.elapsed)
