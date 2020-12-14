from os import system
from time import sleep
from requests import get
from playsound import playsound


# criar umas condicoes para os audios serem tocados
# tocar cada audio umas 3... 5x depois q muda o estado...
# reduzir o tempo do request
connected = True
counter = 0

def play(sound):
    global counter
    if(counter < 3):
        playsound(sound)
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
        play('sounds/wrong.mp3')

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
