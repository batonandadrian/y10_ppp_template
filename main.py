# testing
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
    while instruct_result not in '1 2 3 4 5 6 7 8 9 10 11 12': #user might enter '11 12' and this code wouldn't stop it
        instruct_result = input('Which part of the game would you like to know more? \n1. Pawn \n2. Rook \n3. King \n4. Knight \n5. Queen \n6. Bishop \n7. Legal Moves \n8. Castling \n9. Wins \n10. Losses \n11. Draws \n')
    if instruct_result == '1':
        pass
        #WORK IN PROGRESS

def play():
    print("Let's play!")




def menu():
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    while menu_result not in '12': #user might enter '12' and this code wouldn't support it
        clear()
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    if menu_result == '1':
        instructions()
    else:
        play()
menu()