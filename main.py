# Chess 960
import random
from colorama import Fore
import os
#print(Fore.RED + 'This text is red in color')
def main():
    menu()

def clear():
    os.system('clear')

def instructions():
    clear()
    
def menu():
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    while menu_result not in '12':
        clear()
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    if menu_result == '1':
        instructions()
menu()