# testing
# Chess 960
import random
from colorama import Fore
import os
#print(Fore.RED + 'This text is red in color')
# Default to empty board
'''
TASKS:
- ADD try: except: and while: to prevent errors
- ADD movement restrictions
- ADD turn restrictions
'''
#git stage *
#git commit -m "message"
#git push

def main():
    '''Opens up the menu'''
    names = ['', '']
    board = [['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']]

    #board[0] is row 8 and board[-1] is row 1
    menu_result = menu()
    if menu_result == '1':
        instructions()
        menu_result = menu()
    elif menu_result == '2':
        names = setup_players()
        board = setup_board()

    '''Starts with white's turn'''
    game_in_progress = True
    #while the game hasn't ended, repeat turns
    colour = 'White'
    while game_in_progress:
        start_turn(colour, names, board)
        display_board(board) #not going to work, needs an update_board() function
        turn(colour)

def clear():
    '''Clearing the screen'''
    os.system('clear')

def instructions():
    '''Displays instructions - Checks for which type of thing the user needs help on'''
    clear()
    while instruct_result not in '1 2 3 4 5 6 7 8 9 10 11 12': 
        instruct_result = input('Which part of the game would you like to know more? \n1. Pawn \n2. Rook \n3. King \n4. Knight \n5. Queen \n6. Bishop \n7. Legal Moves \n8. Castling \n9. Wins \n10. Losses \n11. Draws \n')
    if instruct_result == '1':
        pass
        #WORK IN PROGRESS
        #NOT A PRIORITY TO BE WORKED ON

def turn(colour_of_turn):
    '''Makes the turn to the opposite player, allows the opposite player to move and disallows the player who moved to move on the opponent's turn'''
    if colour_of_turn == 'Black':
        colour_of_turn = 'White'
    else:
        colour_of_turn = 'Black'

def start_turn(colour,names,board):
    '''Tells the player of the turn that it is their turn to make a move. Calls move() so that they can start selecting a move'''
    if colour == 'White':
        print(f'{names[0]}, it is your turn to make a move.')
    else:
        print(f'{names[1]}, it is your turn to make a move.')
    move(colour,names,board)

def move(colour,names,board):
    '''Checks if their move is possible and moves it if it is'''
    if colour == 'White': #conditions for white
        start_square = input(f'Where is your starting square, {names[0]}?\n')
        end_square = input(f'Where is your starting square, {names[0]}?\n')
        while False:
            start_square = input(f'Where is your starting square, {names[0]}?\n')
            end_square = input(f'Where is your starting square, {names[0]}?\n')
        #not complete

        return update_board(start_square,end_square,board)
        pass
    else: #conditions for black
        pass #work in progress

def check_piece_at_square(square,board):
    '''Returns the piece at the square when put into the format  "letternumber" '''
    square = str(ord(square[0]) - 97) + square[1] #making the letternumber format into a numbernumber format
    row = int(square[1])
    row = abs(row - 8)

    '''
    When s is 5, row is 3
    When s is 6, row is 2
    When s is 7, row is 1
    When s is 8, row is 0
    '''
    column = int(square[0]) #since the column has been adjusted using ord, it is already correct
    return board[row][column] #returning the piece at the square by getting the row then the column

def edit_square(square,piece,board):
    '''Changes the piece at the square when put into the format  "letternumber" '''
    square = str(ord(square[0]) - 97) + square[1] #making the letternumber format into a numbernumber format
    row = int(square[1])
    row = abs(row - 8)
    column = int(square[0]) 
    board[row][column] = piece #changing the piece at the square
    return board

def setup_players():
    print("Let's play!")
    names = [input('Player 1 (White), enter your name.\n'), input('Player 2 (Black), enter your name.\n')]
    return names

def setup_board():
    '''Creates a new random board'''
    board = random_board(empty_board()) #creates an empty board, then randomises it
    display_board(board) #displays the random board
    return board

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

def update_board(start,end,board):
    '''Takes in a move, updates and returns the board'''
    moving_piece = check_piece_at_square(start,board)
    while moving_piece == '.': #prevents empty squares from moving
        moving_piece = check_piece_at_square(start,board) #checks what piece it is moving from the start
    board = edit_square(end,moving_piece,board) #gets the new board from edit_square after setting the piece on the end square
    board = edit_square(start,'.',board) #sets the square it moved away from to blank
    return board

def random_board(random_board):
    '''Shuffles the pieces, setting the whole row of white and black pieces to the 8th and 1st rank with board[-1] and board[0]'''
    white_shuffle = ['♔', '♕', '♖', '♖', '♗', '♗', '♘', '♘']
    black_shuffle = ['♚', '♛', '♜', '♜', '♝', '♝', '♞', '♞']

    random.shuffle(white_shuffle)
    random.shuffle(black_shuffle)

    random_board[0] = white_shuffle
    random_board[-1] = black_shuffle

    random_board[1] = ['♙'] * 8 #makes the 2nd row from the bottoms pawns
    random_board[-2] = ['♟'] * 8 #makes the 2nd row from the top pawns
    return random_board

def menu():
    '''Starts up a menu to ask the user the instruction to do, then executes based on their choice'''
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    while menu_result not in ['1', '2']:
        print('TEST')
        clear()
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    return menu_result

main()