from os import system, name
from time import sleep

def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac/linux
    else:
        _ = system('clear')

