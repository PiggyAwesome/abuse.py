import requests
import threading

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

url = 'https://discord.black/index.php?/login/='


data = {

' csrfKey': '18548ea8f1b8eeadd0caae496dabf7c1',
'ref': 'aHR0cHM6Ly9kaXNjb3JkLmJsYWNrLw==',
'auth': 'skwll@is.epic',
'password': 'gfyguhvgyfguh',
'_processLogin': 'usernamepassword',


}


def do_request():
    while True:
      feedback = requests.post(url, data=data, headers=headers)
      print(feedback)
do_request()


threads = []

for i in range(5):

 t = threading.Thread(target=do_request())
 t.daemon = True
 threads.append(t)


for i in range(5):
 threads[i].start

for i in range(5):
 threads[i].join
