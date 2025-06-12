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



'''
BUGS NEEDED TO FIX:
for some reason, square is 1 digit ( when you move a rook horizontally)
this crashes the program beacause square[1] is not a thing
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
                if rook_conditions(start_square,end_square,board,colour) == True: #if rook moves are checked and legal
                    conditions_met = True
            display_board(board)
        #not complete

        return update_board(start_square,end_square,board)
    else: #conditions for black
        pass #work in progress

def check_piece_at_square(square, board):
    '''Returns the piece at the square when put into the format "letternumber" '''
    square_indices = turn_notation_compatible(square)  #convert square into usable notation

    row = square_indices[1]    # row index
    column = square_indices[0]  # column index
    try:
        return board[row][column]  # returns the piece at row and column
    except IndexError:
        print(f'Row was {row}, column was {column}')

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
    if start == end: #can't move to same squares
        return 'Not supported'
    elif start[0] == end[0]: #if column is the same
        info = pieces_in_between(start,end,'vertical',board) #returns the pieces in between and the direction of travel (up down left right)
        direction = info[1]
        pieces = info[0]
        if move_limits(pieces,direction,start,end,colour) == True:
            return True
        else:
            return False
    elif start[1] == end[1]: #if row is the same
        info = pieces_in_between(start,end,'horizontal',board) #returns the pieces in between and the direction of travel (up down left right)
        direction = info[1]
        pieces = info[0]
        if move_limits(pieces,direction,start,end,colour) == True: #if moving to the square is allowed
            return True
        else:
            return False
    else: #not moving straight
        return 'Not supported'
def bishop_conditions(start,end,board,colour):
    pass

def pieces_in_between(start,end,mode,board):
    '''
    Has 3 modes, vertical, horizontal, diagonal. 
    Uses the board to check (exclusive) of any piece in between other pieces
    '''


    if mode == 'vertical': #checks the rows
        #code below turns chess square notation eg 'e4'
        #into row, column notation
        start_row = turn_notation_compatible(start)[1]
        start_column = turn_notation_compatible(start)[0]
        end_row = turn_notation_compatible(end)[1]
        end_column = turn_notation_compatible(end)[0]
        #vertical means it iterates through the same column, different row
        pieces_between = []
        #print(f'END ROW = {end_row}, START ROW = {start_row}') #testing only
        if end_row > start_row: #if it is moving downwards
            #turn_notation compatible reverses it. larger row = smaller row
            #print('TEST zz')
            step = 1 #if you +1 to the start_row, then the row decreases
            direction = 'down'
        else:
            step = -1
            direction = 'up'
            #print('TEST z')
        #print('TEST 1')
            #iterate forwards
        for row in range(start_row + step,end_row + step,step): #exclusive of starting square
            #print('TEST 12')
            square = chr(start_column+97) + str(8-row) #converts the square back into chess notation, column is constant
            piece_at_square = check_piece_at_square(square,board)
            pieces_between.append(piece_at_square) #adds the piece at the square to the list
            #print('HI'+check_piece_at_square(square,board))
        print(pieces_between)
        return [pieces_between,direction]
    

    elif mode == 'horizontal':
        #code below turns chess square notation eg 'e4'
        #into row, column notation
        start_row = turn_notation_compatible(start)[1]
        start_column = turn_notation_compatible(start)[0]
        end_row = turn_notation_compatible(end)[1]
        end_column = turn_notation_compatible(end)[0]
        #vertical means it iterates through the same column, different row
        pieces_between = []
        #print(f'END ROW = {end_row}, START ROW = {start_row}') #testing only
        if end_column > start_column: #if it is moving to the right
            #print('TEST zz')
            step = 1 #if you +1 to the start_row, then the row decreases
            direction = 'right'
        else:
            step = -1
            direction = 'left'
            #print('TEST z')
        #print('TEST 1')
            #iterate forwards
        for column in range(start_column + step,end_column + step,step): #exclusive of starting square. inclusive of ending square
            #print('TEST 12')
            square = chr(start_column+97+column) + str(8-start_row) #converts the square back into chess notation. row is constant
            piece_at_square = check_piece_at_square(square,board)
            pieces_between.append(piece_at_square) #adds the piece at the square to the list
            #print('HI'+check_piece_at_square(square,board))
        print(pieces_between)
        return [pieces_between,direction]
    

    else: #mode = diagonal
        pass

def move_limits(pieces_in_between, direction, start_square, end_square, colour):
    '''Finds the furthest square to move to, based on the direction of movement and the square the user wants to move from and to.'''
    white_pieces = ['♔', '♕', '♖', '♖', '♗', '♗', '♘', '♘','♙']
    black_pieces = ['♚', '♛', '♜', '♜', '♝', '♝', '♞', '♞','♟']
    if direction == 'right' or 'up':
        step = 1
    else:
        step = -1
    furthest = 0
    start = turn_notation_compatible(start_square)
    for square in pieces_in_between:
        if square == '.': #if the square is empty, extend the furthest square possible
            furthest += step
        elif square in white_pieces: #if the piece is white at the square
            if colour == 'White':
                break #furthest it can move
            else: #colour is black
                furthest += step #furthest includes taking the white piece
        else: #square in black pieces
            if colour == 'Black':
                furthest += step
            else:
                break
    if direction == 'up' or direction == 'down': #add furthest to row.
        furthest_square = int(str(start[0]) + str(start[1] + furthest))
        print(f'TEST: {furthest_square} and {turn_notation_compatible(furthest_square)} and {reverse_notation(furthest_square)}') #TESTING ONLY
        furthest_square = reverse_notation(furthest_square)
        if int(end_square[1]) > furthest_square[1]:
            print(f'You cannot move to {end_square}. The furthest you can move to with that piece is {furthest_square}')
            return False
        else:
            return True
        
    elif direction == 'right' or direction == 'left': #adds furthest to column
        furthest_square = int(str(start[0] + furthest) + str(start[1]))
        #FURTHEST SQUARE IS ALREADY NI COMPATIBLE FORM
        print(f'TEST: {furthest_square} and {reverse_notation(furthest_square)}') #TESTING ONLY
        furthest_square = reverse_notation(furthest_square)
        print(type(furthest_square[0]),type(end_square[0]))
        print(end_square,furthest_square)
        if int(ord(end_square[0])) > int(ord(furthest_square[0])): #if the square the user wants to move to is further than what is possible
            print(f'You cannot move to {end_square}. The furthest you can move to with that piece is {furthest_square}')
            return False #move not legal
        else:
            return True
    # print(f'When you tried to move from {start_square} to {end_square}, the furthest you could move to was {furthest_square}') #TESTING
    



def turn_notation_compatible(square):
    square = str(square)
    if len(square) != 2:
        print(f'Square is {len(square)} digits long, and the value is {square}')
        #raise ValueError
    

    '''Turns chess notation into row, columns so that it can be found on the chessboard using board[row][column]'''
    column = ord(square[0]) - 97  #csonvert letter to index (0-7)
    row = 8 - int(square[1])  # convert number to index (0-7)
    
    return [column, row]  # RETURN AS A LIST OF COLUMN AND ROW


def reverse_notation(square):
    '''Turns nottion in row, column back into chess notation'''
    square = str(square)
    if len(square) != 2:
        print(f'Square is {len(square)} digits long, and the value is {square}')
        #raise ValueError
    print(f'SQUARE IS {square}') #TESTING ONLY
    new_row = 8 - int(str(square)[1])
    new_column = chr(int(str(square)[0]) + 97)
    return [new_column,new_row]
main()



