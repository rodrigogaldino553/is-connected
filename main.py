from os import system
from time import sleep
from requests import get
from playsound import playsound as play


def clear():
    system('clear')


def connect(url):
    try:
        site = get(url)
        clear()

    except:
        clear()
        print('\033[2;31mERROR! INTERNET UNAVAILABLE!\033[m')

    else:
        print('\033[2;32mYOU ARE CONNECTED!\033[m')
        

url_google = 'https://google.com'
print('requesting...')

while True:
    connect(url_google)
    sleep(5)
    clear()
    print('requesting...')
