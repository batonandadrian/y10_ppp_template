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
- ADD turn restrictions (can't move from the same square to the same square)
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
    



    #TESTING
    




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
        colour = turn(colour)

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
    return colour_of_turn

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
        conditions_met = False
        while conditions_met == False:  #repeatedly asks user squares until all the requirements are fulfilled
            start_square = input(f'Where is your starting square, {names[0]}?\n').lower()
            end_square = input(f'Where is your end square, {names[0]}?\n').lower()
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            # used to skip legal moves while it is not finished
            conditions_met = True # TESTING PURPOSES ONLY !!! REMOVE AT THE END!!!!
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            if check_piece_at_square(start_square,board) == '♔': #if the piece being moved is a king
                if king_conditions(start_square,end_square,board,colour) == True: #if move is legal and checked
                    conditions_met = True
            elif check_piece_at_square(start_square,board) == '♖':
                pieces_in_between(start_square,end_square,'vertical',board)
        #not complete

        return update_board(start_square,end_square,board)
    else: #conditions for black
        pass #work in progress

def check_piece_at_square(square,board, mode='normal'):
    '''Returns the piece at the square when put into the format  "letternumber" '''
    if mode == 'normal': #not normal mode allows you to input in the format number number
        square = turn_notation_compatible(square)
    else:
        square = str(square)
    return board[int(square[1])][int(square[0])] #returning the piece at the square by getting the row then the column

def edit_square(square,piece,board):
    '''Changes the piece at the square when put into the format  "letternumber" '''
    square = turn_notation_compatible(square)
    board[square[1]][square[0]] = piece #changing the piece at the square
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
    #clear() FOR TESTING ONLY! REMOVE # after complete
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

    random_board[-1] = white_shuffle
    random_board[0] = black_shuffle

    random_board[-2] = ['♙'] * 8 #makes the 2nd row from the bottoms pawns
    random_board[1] = ['♟'] * 8 #makes the 2nd row from the top pawns
    return random_board

def menu():
    '''Starts up a menu to ask the user the instruction to do, then executes based on their choice'''
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    while menu_result not in ['1', '2']:
        print('TEST')
        #clear() TESTING ONLY! REMOVE # WHEN COMPLETE
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    return menu_result

def king_conditions(start,end,board,colour):
    pass

def queen_conditions(start,end,board,colour):
    #could combine rook and bishop conditions
    if rook_conditions() or bishop_conditions():
        return True
    pass

def pawn_conditions(start,end,board,colour):
    pass

def knight_conditions(start,end,board,colour):
    pass

def rook_conditions(start,end,board,colour):
    pass

def bishop_conditions(start,end,board,colour):
    pass

def pieces_in_between(start,end,mode,board):
    '''
    Has 3 modes, vertical, horizontal, diagonal. 
    Uses the board to check (exclusive) of any piece in between other pieces
    '''
    print('TEST 2')
    if mode == 'vertical': #checks the rows
        print('TEST v')
        #code below turns chess square notation eg 'e4'
        #into row, column notation
        start_row = turn_notation_compatible(start)[1]
        start_column = turn_notation_compatible(start)[0]
        end_row = turn_notation_compatible(end)[1]
        end_column = turn_notation_compatible(end)[0]
        #vertical means it iterates through the same column, different row
        pieces_between = []
        print(f'END ROW = {end_row}, START ROW = {start_row}') #testing only
        if end_row > start_row: #if it is moving downwards
            #turn_notation compatible reverses it. larger row = smaller row
            print('TEST zz')
            step = 1 #if you +1 to the start_row, then the row decreases
        else:
            step = -1
            print('TEST z')
        print('TEST 1')
            #iterate forwards
        for row in range(start_row + step,end_row ,step): #exclusive of starting square
            print('TEST 12')
            square = chr(start_column+97) + str(8-row) #converts the square back into chess notation
            piece_at_square = check_piece_at_square(square,board)
            pieces_between.append(piece_at_square) #adds the piece at the square to the list
            print('HI'+check_piece_at_square(square,board))
        print(pieces_between)
        return pieces_between
    elif mode == 'horizontal':
        pass
    else: #mode = diagonal
        pass

def turn_notation_compatible(square):
    '''Turns chess notation into row, columns so that it can be found on the chessboard using board[row][column]'''
    row = int(square[1])
    row = abs(row - 8) #convert to board index 0-7
    column = (ord(square[0]) - 97)
    #print([column, row]) #TESTING ONLY! REMOVE AFTER FINISHED
    return [column, row]
main()