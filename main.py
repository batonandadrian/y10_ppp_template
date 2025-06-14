# testing
# Chess 960
import random
from colorama import Fore, Back, Style
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
fix try and except for user inputs
'''
#git stage *
#git commit -m "message"
#git push

#GLOBAL
white_pieces = ['♔', '♕', '♖', '♗', '♘', '♙']
black_pieces = ['♚', '♛', '♜', '♝', '♞', '♟']

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
            #conditions_met = True # TESTING PURPOSES ONLY !!! REMOVE AT THE END!!!!
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            if check_piece_at_square(start_square,board) == '♚': #if the piece being moved is a king
                if king_conditions(start_square,end_square,board,colour) == True: #if move is legal and checked
                    conditions_met = True
                else:
                    print(Back.RED + Fore.BLACK + f'The king could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
            elif check_piece_at_square(start_square,board) == '♜':
                if rook_conditions(start_square,end_square,board,colour) == True: #if rook moves are checked and legal
                    conditions_met = True
                else:
                    print(Back.RED + Fore.BLACK + f'The rook could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
            elif check_piece_at_square(start_square,board) == '♟':
                if pawn_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.RED + Fore.BLACK + f'The pawn could not move to {end_square}.' + Style.RESET_ALL)
            elif check_piece_at_square(start_square,board) == '♞':
                if pawn_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.RED + Fore.BLACK + f'The pawn could not move to {end_square}.' + Style.RESET_ALL)
                
            # display_board(board)
        #not complete

        return update_board(start_square,end_square,board)
    else: #conditions for black
        pass

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
    if start == end:
        test('Start is same as end')
        return False #can't move to same square

    #cant capture own pieces
    if colour == 'White':
        test('Pawn is white')
        if check_piece_at_square(end,board) in white_pieces:
            test('self capture')
            return False

        elif start[0] == end[0]: #same column
            test('column is the same')
            pieces, _ = pieces_in_between(start,end,'vertical',board) #gets piecesinbetween[0]
            print(pieces)
            empty_squares_only = True
            for square in pieces:
                test(square)
                if square not in ['.','',' ', None]:  
                    empty_squares_only = False
                    test('pieces in between')
                    return False
            if empty_squares_only:
                test('squares between are empty')
                if int(end[1]) - int(start[1]) == 2:
                    if start[1] == '2':  # White pawns start from rank 2
                        return True
                    else:
                        return False
                elif int(end[1]) - int(start[1]) == 1:  # normal 1-square move
                    return True

        elif abs(ord(start[0]) - ord(end[0])) == 1: #captures have 1 column difference
            test('column difference = 1')
            if check_piece_at_square(end,board) in black_pieces: #if end square is black pieces, and column diff is 1 then it is a capture
                if int(end[1]) - int(start[1]) == 1:
                    return True
            # TODO: EN PASSANT
            return False

        else:
            test('movement not possible')
            return False

    else: # Black pawn
        test('Pawn is black')
        if check_piece_at_square(end,board) in black_pieces:
            test('self capture')
            return False

        elif start[0] == end[0]:
            test('column is the same')
            pieces = pieces_in_between(start,end,'vertical',board)
            print(pieces)
            empty_squares_only = True
            for square in pieces:
                test(square)
                if square not in ['.','',' ', None]:  # <-- same fix
                    empty_squares_only = False
                    test('pieces in between')
                    return False
            if empty_squares_only:
                test('squares between are empty')
                if int(start[1]) - int(end[1]) == 2:  # <-- reverse for black
                    if start[1] == '7':
                        return True
                    else:
                        return False
                elif int(start[1]) - int(end[1]) == 1:  # normal 1-square move
                    return True

        elif abs(ord(start[0]) - ord(end[0])) == 1:
            test('column difference = 1')
            if check_piece_at_square(end,board) in white_pieces:
                if int(start[1]) - int(end[1]) == 1: 
                    return True
            # TODO: EN PASSANT
            return False

        else:
            test('movement not possible')
            return False


def knight_conditions(start,end,board,colour):
    if start == end:
        return False  # Can't move to the same square
    if colour == 'White':
        if check_piece_at_square(end,board) in white_pieces: #if your colour is white, you cannot capture own pieces
            return False
    else:
        if check_piece_at_square(end,board) in black_pieces:
            return False
    start_column, start_row = start #multi variable assignment
    end_column, end_row = end
    if abs(ord(end_column) - ord(start_column)) == 1: #Case 1:Forward and backward knight moves
        if abs(end_row - start_row) == 2: #Should be 2 if it moves up and down L shape
            return True
        else:
            return False
    elif abs(ord(end_column) - ord(start_column)) == 2: #Case 2: Left right knight moves
        if abs(end_row - start_row) == 1: #Should be 1 if it moves sideways L shape
            return True
        else:
            return False
    else:
        return False

def rook_conditions(start, end, board, colour):
    # Check if the start and end squares are the same
    if start == end:
        return False  # Can't move to the same square
    if colour == 'White':
        if check_piece_at_square(end,board) in white_pieces: #if your colour is white, you cannot capture own pieces
            return False
    else:
        if check_piece_at_square(end,board) in black_pieces:
            return False
    # Check for vertical movement
    if start[0] == end[0]:  # Same column
        pieces = pieces_in_between(start, end, 'vertical', board)
        
        # Ensure all pieces between the start and end are empty
        for piece in pieces:
            if piece != '.': #if the square is not empty
                return False  # Blocked by another piece
        direction = pieces[1]
        pieces = pieces[0]
        if move_limits(pieces,direction,start,end,colour) == True:
            return True
        else:
            return False

    # Check for horizontal movement
    elif start[1] == end[1]:  # Same row
        info = pieces_in_between(start, end, 'horizontal', board)
        
        # Ensure all pieces between the start and end are empty
        for piece in info:
            if piece != '.':
                return False  # Blocked by another piece
        direction = info[1]
        pieces = info[0]
        if move_limits(pieces,direction,start,end,colour) == True:
            return True
        else:
            return False
    
    return False  #invalid move (not straight)

def bishop_conditions(start,end,board,colour):
    pass

def pieces_in_between(start, end, mode, board):
    start_row, start_column = turn_notation_compatible(start) #makes start row and column into compatible notation[0] and [1]
    end_row, end_column = turn_notation_compatible(end)

    pieces_between = []

    if mode == 'horizontal':
        if end_column > start_column: #if moving right
            step = 1
            direction = 'right'
        else:
            step = -1 #if moving left
            direction = 'left'
        
        for column in range(start_column + step, end_column, step):  # Exclusive of start and end
            square = chr(column + 97) + str(8 - start_row)  # Convert back to chess notation
            piece_at_square = check_piece_at_square(square, board)
            pieces_between.append(piece_at_square)

    elif mode == 'vertical':
        if end_row > start_row: #moving down
            step = 1
            direction = 'down'
        else:
            step = -1
            direction = 'up'
        
        for row in range(start_row + step, end_row + step, step):  # Exclusive of start 
            square = chr(start_column + 97) + str(8 - row)  # Convert back to chess notation
            piece_at_square = check_piece_at_square(square, board)
            pieces_between.append(piece_at_square)
    else: #mode = diagonal
        pass
    return [pieces_between,direction]  #return pieces in between
    

def move_limits(pieces_in_between, direction, start_square, end_square, colour):
    '''Finds the furthest square to move to, based on the direction of movement and the square the user wants to move from and to.'''
    white_pieces = ['♔', '♕', '♖', '♖', '♗', '♗', '♘', '♘','♙']
    black_pieces = ['♚', '♛', '♜', '♜', '♝', '♝', '♞', '♞','♟']
    if direction in ['right', 'up']:
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
        furthest_square = int(str(start[0] + str(start[1] + furthest))) #error 
        print(f'TEST: {furthest_square} and {turn_notation_compatible(furthest_square)} and {reverse_notation(furthest_square)}') #TESTING ONLY
        furthest_square = reverse_notation(furthest_square)
        if int(end_square[1]) > furthest_square[1]:
            print(f'You cannot move to {end_square}. The furthest you can move to with that piece is {furthest_square}')
            return False
        else:
            return True
            test('up or down returned true')
        
    elif direction == 'right' or direction == 'left': #adds furthest to column
        furthest_square = int(str(start[0] + furthest) + str(start[1])) #error on this line
        #FURTHEST SQUARE IS ALREADY NI COMPATIBLE FORM
        print(f'Test {furthest_square}')
        print(f'TEST: {furthest_square} and {reverse_notation(furthest_square)}') #TESTING ONLY
        furthest_square = reverse_notation(furthest_square)
        print(type(furthest_square[0]),type(end_square[0]))
        print(end_square,furthest_square)
        if int(ord(end_square[0])) > int(ord(furthest_square[0])): #if the square the user wants to move to is further than what is possible
            print(f'You cannot move to {end_square}. The furthest you can move to with that piece is {furthest_square}')
            return False #move not legal
        else:
            return True
            test('Right or left, returned true')

    print(f'When you tried to move from {start_square} to {end_square}, the furthest you could move to was {furthest_square}') #TESTING
    



def turn_notation_compatible(square):
    square = str(square)
    
    # error if its not 2 digits (prevents it from working)
    if len(square) != 2:
        raise ValueError(f'Square must be in the format "letternumber", received: {square}')
    
    # convert letter to index (0-7)
    column = ord(square[0]) - ord('a')  
    
    # Convert number to index (0-7)
    row = 8 - int(square[1])  
    
    return [column, row]  #return as a list of column and row indices




def reverse_notation(square):
    '''Turns notation in row, column back into chess notation'''
    square = str(square)
    if len(square) != 2:
        print(f'Square is {len(square)} digits long, and the value is {square}')
        #raise ValueError
    print(f'SQUARE IS {square}') #TESTING ONLY
    new_row = 8 - int(str(square)[1])
    new_column = chr(int(str(square)[0]) + 97)
    return [new_column,new_row]

def test(message):
    '''To make it clear that a print message is for testing purposes'''
    print(Fore.MAGENTA + f'{message}\n' + Style.RESET_ALL)
main()



