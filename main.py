from os import system
from time import sleep
from requests import get
from playsound import playsound



connected = True
counter = 0

def play(sound):
    global counter
    if(counter < 3):
        try:
            playsound(sound)

        except:
            print('\033[2;31mError! cannot play alert sound!\033[m')
            clear()
            print('EXECUTE THE PROGRAM "main.py" FROM "is-connected" FOLDER ON YOUR TERMINAL')
            sleep(3)


        counter += 1


def clear():
    system('clear')


def connect(url):
    global connected
    global counter
    try:
        site = get(url)
        clear()
        if not connected:
            counter = 0

        connected = True

    except:
        clear()
        if connected:
            counter = 0

        connected = False
        print('\033[2;31mERROR! INTERNET UNAVAILABLE!\033[m')
        play('./sounds/wrong.mp3')

    else:
        print('\033[2;32mYOU ARE CONNECTED!\033[m')
        play('sounds/good_news.mp3')
        

url = 'https://python.org'
clear()
print('requesting...')

while True:
    connect(url)
    sleep(5)
    clear()
    print('requesting...')
    