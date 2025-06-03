# testing
# Chess 960
import random
from colorama import Fore
import os
#print(Fore.RED + 'This text is red in color')

'''Globals '''
# Default to empty board



def main():
    '''Opens up the menu'''
    board = [['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]
    menu_result = menu()
    while menu_result not in ['1','2']: #user might enter '12' and this code wouldn't support it
        clear()
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    if menu_result == '1':
        instructions()
    else:
        play(board)
    menu(board)

def clear():
    '''Clearing the screen'''
    os.system('clear')

def instructions():
    '''Displays instructions - Checks for which type of thing the user needs help on'''
    clear()
    while instruct_result not in '1 2 3 4 5 6 7 8 9 10 11 12': #user might enter '11 12' and this code wouldn't stop it
        instruct_result = input('Which part of the game would you like to know more? \n1. Pawn \n2. Rook \n3. King \n4. Knight \n5. Queen \n6. Bishop \n7. Legal Moves \n8. Castling \n9. Wins \n10. Losses \n11. Draws \n')
    if instruct_result == '1':
        pass
        #WORK IN PROGRESS
        #NOT A PRIORITY TO BE WORKED ON

def play(board):
    '''Inputs names from user - starts up a new board'''
    print("Let's play!")
    names = [input('Player 1 (White), enter your name.\n'), input('Player 2 (Black), enter your name.\n')]
    board = random_board(board)
    display_board(board)

def empty_board():
    '''Uses for loops to create an empty board, with numbers and letters to display row and column'''
    board = [['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.']]
    return board
def display_board(board):
    '''Display board'''
    clear()
    current_column = ord('A')
    current_row = 8
    for line in board:
        print(f"{current_row} {" ".join(line)}")
        current_row -= 1
    
    # Generate the column display
    column_display = ""
    board_length = len(board[0])

    for i in range(board_length):
        column_display += chr(current_column) + " "
        current_column += 1

    print(f"  {column_display}")

def random_board(board):
    white_shuffle = ['♔', '♕', '♖', '♖', '♗', '♗', '♘', '♘']
    black_shuffle = ['♚', '♛', '♜', '♜', '♝', '♝', '♞', '♞']

    random.shuffle(white_shuffle)
    random.shuffle(black_shuffle)

    board[-1] = white_shuffle
    board[0] = black_shuffle

    board[-2] = ['♙'] * 8
    board[1] = ['♟'] * 8
    return board
def menu():
    '''Starts up a menu to ask the user the instruction to do, then executes based on their choice'''
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    return menu_result

menu()