import requests
import time

def internet_connection():
    try:
        response = requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False    


while not internet_connection():
    internet_connection()
    time.sleep(10)

print(time.strftime("%H:%M:%S, %d/%m", time.localtime(time.time())))
