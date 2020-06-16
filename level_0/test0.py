#!/usr/bin/python3
import requests
from colorama import Fore

url = 'http://158.69.76.135/level0.php'
myobj = {'id': '12', 'holdthedoor': 'Submit'}

for i in range(1, 10):
    requests.post(url, data=myobj)
    print(Fore.YELLOW +"voting for: {}, I've done {} votes".format(myobj.get("id"), i))
print(Fore.GREEN + "I've done {} votes, by the user {}".format(i, (myobj.get("id"))))
