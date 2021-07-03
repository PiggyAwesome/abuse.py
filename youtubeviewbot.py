import requests
import threading

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'



def do_request():
    while True:
      response = requests.get(url)
      print(response)



threads = []

for i in range(500):

 t = threading.Thread(target=do_request())
 t.daemon = True
 threads.append(t)


for i in range(500):
 threads[i].start

for i in range(500):
 threads[i].join
