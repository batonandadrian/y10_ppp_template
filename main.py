# testing
# Chess 960
import random
from colorama import Fore, Back, Style
import os
#print(Fore.RED + 'This text is red in color')
# Default to empty board
'''
TASKS (HIGH TO LOW PRIORITY):
- Finish CHECK and CHECKMATE
- LOGIC FOR CHECk:
 - Iterating through the board to check for each piece. If the piece can currently move to the king's position:
   - Then the king is in check
   - Otherwise, the king is not in check

- LOGIC FOR CHECKMATE
 - CHECK IF the opposing KING is currently in check
  - IF not, return False
  - IF yes, find each empty square or square occupied by opposite coloured piece to the king the king can move to
   - Iterate through each square the opposing king can move to
    - Use check() to find if any piece is checking each of the squares around the king
    - If a square next to the king is being checked, that means the king cannot move there
  - If every single available square that the king can move to, AND the king is currently in check, it is a checkmate

- LOGIC FOR CHECKING PIECES AROUND KING (CURRENTLY DOING)
 - Having a list with tuples of stuff around the king:
  - possible_squares = [(-1,-1),(0,-1),(1,-1),(-1,0)...] <- reflects this [topleft,topmiddle,topright...]
   - Using for loops, iterating through all of them
   - Then having a thing that adds it to compatible notation row and column  Eg. row += possible_squares[i][1] (changes the row according to the possible square cases)



- ALL Chess Features
  - EN PASSANT
  - CASTLING (CHECK pieces in between, move rook 2 squares and king 2 squares)
  - CHECKS (Has to make a move that stops the check, if none then it is checkmate (maybe surrendering instead of checkmate))
    - Determining the valid moves for each opponent's piece.
    - Checking if any of those valid moves land on the square occupied by the king.
- ADD turns (white move, black move) CORRECTLY [V]






(ALL OPTIONAL)
- Message when you are in check (by checking if the last move put you in check (discovered checks etc wouldn't fit))
- Possibly Checkmate
- Illegal move error messages
- INSTRUCTIONS, tutorial boards
- IMPROVE interface (icons, emojis, board outline?)
- IMPROVE quality (having better print messages, showing which piece you want to move when you get the square of it)
- ADD toggleable clocks for each side (maybe not)
- ADD settings (settings to toggle clocks, time for each side, highlight possible squares, background colour)
- POLISH and remove test messages once done
'''

'''
COMPLETED:
- restrictions for all pieces (except king)
- movement system

'''

'''
BUGS NEEDED TO FIX:
fix try and except for user inputs
'''
#git stage *
#git commit -m "message"
#git push

black_pieces = ['♔', '♕', '♖', '♗', '♘', '♙']
white_pieces = ['♚', '♛', '♜', '♝', '♞', '♟']

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
        # #not going to work, needs an update_board() function
        colour = turn(colour)
        king_pos = find_king_pos(board,colour)
        test(f'King pos is {king_pos}')
        check_squares_around_king(king_pos,board,colour)
        
def clear():
    '''Clearing the screen'''
    os.system('clear')

def instructions():
    '''Displays instructions - Checks for which type of thing the user needs help on'''
    clear()
    instruct_result = int(input('Which part of the game would you like to know more? \n1. Pawn \n2. Rook \n3. King \n4. Knight \n5. Queen \n6. Bishop \n7. Legal Moves \n8. Castling \n9. Wins \n10. Losses \n11. Draws \n'))
    while instruct_result not in [1,2,3,4,5,6,7,8,9,10,11]:
        instruct_result = int(input('Which part of the game would you like to know more? \n1. Pawn \n2. Rook \n3. King \n4. Knight \n5. Queen \n6. Bishop \n7. Legal Moves \n8. Castling \n9. Wins \n10. Losses \n11. Draws \n'))
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
            display_board(board)
            test('white')
            start_square = input(f'Where is your starting square, {names[0]}?\n').lower()
            print(f'I see you are trying to move the {check_piece_at_square(start_square,board)}  on {start_square}.')
            end_square = input(f'Where is your end square, {names[0]}?\n').lower()
            test(check_piece_at_square(start_square,board))
            test(check_piece_at_square(end_square,board))
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            # used to skip legal moves while it is not finished
            #conditions_met = True # TESTING PURPOSES ONLY !!! REMOVE AT THE END!!!!
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            
            
            if check_piece_at_square(start_square,board) == '♚': #if the piece being moved is a king
                if king_conditions(start_square,end_square,board,colour) == True: #if move is legal and checked
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The king could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
            elif check_piece_at_square(start_square,board) == '♜':
                if rook_conditions(start_square,end_square,board,colour) == True: #if rook moves are checked and legal
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The rook could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♟':
                if pawn_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The pawn could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
                    
            elif check_piece_at_square(start_square,board) == '♞':
                if knight_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The knight could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♝':
                if bishop_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The bishop could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♛':
                if queen_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The queen could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            if conditions_met == True: #if piece specific legal conditions are met
                #checks for more things
                if no_move_check(start_square,end_square) == False:
                    print(Back.BLUE + Fore.WHITE + f'Stop trying to move your {check_piece_at_square(start_square, board)}  from {start_square} to {end_square}!' + Style.RESET_ALL)
                    conditions_met = False
                    display_board(board)
                elif check_piece_at_square(end_square,board) in white_pieces: #prints illegal move message if move pattern is legal but self capturing
                    print(Back.BLUE + Fore.WHITE + f'Why is your {check_piece_at_square(start_square, board)}  trying to capture your own {check_piece_at_square(end_square,board)}  at {end_square}?' + Style.RESET_ALL)
                    conditions_met = False
                    display_board(board)
                
            if check_check(board,colour): #check if its own king in check
                if checkmate(board,colour):
                    end_game()
                
            if opposite_turn_movement(start_square,board,colour) == False:
                conditions_met = False

        test('board update')
        return update_board(start_square,end_square,board)
    
    else: #conditions for black
        test('black')
        conditions_met = False
        while conditions_met == False:  #repeatedly asks user squares until all the requirements are fulfilled
            test('black')
            display_board(board)
            start_square = input(f'Where is your starting square, {names[1]}?\n').lower()
            print(f'I see you are trying to move the {check_piece_at_square(start_square,board)}  on {start_square}.')
            end_square = input(f'Where is your end square, {names[1]}?\n').lower()
            test(check_piece_at_square(start_square,board))
            test(check_piece_at_square(end_square,board))
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            # used to skip legal moves while it is not finished
            #conditions_met = True # TESTING PURPOSES ONLY !!! REMOVE AT THE END!!!!
            '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
            
            
            if check_piece_at_square(start_square,board) == '♔': #if the piece being moved is a king
                if king_conditions(start_square,end_square,board,colour) == True: #if move is legal and checked
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The king could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
            elif check_piece_at_square(start_square,board) == '♖':
                if rook_conditions(start_square,end_square,board,colour) == True: #if rook moves are checked and legal
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The rook could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♙':
                if pawn_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The pawn could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)
                    
            elif check_piece_at_square(start_square,board) == '♘':
                if knight_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The knight could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♗':
                if bishop_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The bishop could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            elif check_piece_at_square(start_square,board) == '♕':
                if queen_conditions(start_square,end_square,board,colour) == True:
                    conditions_met = True
                else:
                    print(Back.BLUE + Fore.BLACK + f'The queen could not move to {end_square}.' + Style.RESET_ALL)
                    display_board(board)

            if conditions_met == True: #if piece specific legal conditions are met
                #checks for more things
                if no_move_check(start_square,end_square) == False:
                    print(Back.BLUE + Fore.WHITE + f'Stop trying to move your {check_piece_at_square(start_square, board)}  from {start_square} to {end_square}!' + Style.RESET_ALL)
                    conditions_met = False
                    display_board(board)
                elif check_piece_at_square(end_square,board) in black_pieces: #prints illegal move message if move pattern is legal but self capturing
                    print(Back.BLUE + Fore.WHITE + f'Why is your {check_piece_at_square(start_square, board)}  trying to capture your own {check_piece_at_square(end_square,board)}  at {end_square}?' + Style.RESET_ALL)
                    conditions_met = False
                    display_board(board)
            
            if opposite_turn_movement(start_square,board,colour) == False:
                conditions_met = False

        return update_board(start_square,end_square,board)

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

'''Finish subroutines below here.'''
def end_game(colour):
    '''The game ends when someone is checkmated'''

    pass

def check_check(board, colour):
    '''Checks for checks for a king'''
    if colour == 'White':
        king_symbol = '♚'
        opponent_pieces = black_pieces
        opponent_colour = 'Black'
    else:
        king_symbol = '♔'
        opponent_pieces = white_pieces
        opponent_colour = 'White'
    king_square = find_king_pos(board, colour)
    for row_index in range(8):
        for col_index in range(8):
            piece = board[row_index][col_index]
            if piece in opponent_pieces:
                start_square = chr(col_index + ord('a')) + str(8 - row_index)
                if piece == ('♝' if colour == 'White' else '♗'): #more efficient, changes the colour of the piece depending on the colour on one line
                    if bishop_conditions(start_square, king_square, board, opponent_colour):
                        return True
                elif piece == ('♜' if colour == 'White' else '♖'):
                    if rook_conditions(start_square, king_square, board, opponent_colour):
                        return True
                elif piece == ('♛' if colour == 'White' else '♕'):
                    if queen_conditions(start_square, king_square, board, opponent_colour):
                        return True
                elif piece == ('♞' if colour == 'White' else '♘'):
                    if knight_conditions(start_square, king_square, board, opponent_colour):
                        return True
                elif piece == ('♙' if colour == 'White' else '♟'):
                    if pawn_conditions(start_square, king_square, board, opponent_colour):
                        return True
                elif piece == ('♔' if colour == 'White' else '♚'):
                    king_moves = check_squares_around_king(start_square, board, opponent_colour)
                    if king_square in king_moves: 
                        return True
    return False

def checkmate(board, colour):
    if not check_check(board, colour):
        return False
    king_square = find_king_pos(board, colour)
    possible_moves = check_squares_around_king(king_square, board, colour)
    if not possible_moves:
        return True
    for move in possible_moves:
        temp_board = [row[:] for row in board] #creating a new 2d list, an iterating through it
        temp_board = edit_square(move, check_piece_at_square(king_square, temp_board), temp_board)
        temp_board = edit_square(king_square, '.', temp_board)
        if not check_check(temp_board, colour):
            return False
    return True



def find_king_pos(board,colour):
    '''Finds the square of the king on the board in chess notation'''
    #iterate through the board
    if colour == 'White':
        king = '♚'
    else:
        king = '♔'
    row_index = -1
    column_index = -1
    for row in board:
        row_index += 1
        for column in row:
            column_index += 1
            if column == king:
                location = reverse_notation(int(str(column_index) + str(row_index)))
                location = location[0] + str(location[1])
                test(f'Test is {location}')
    return location

def check_squares_around_king(king_square,board,colour):
    '''Returns a list of squares the opposing king is able to move to '''
    possible_squares = []
    top_left_square = turn_notation_compatible(king_square)
    top_left_square = int(str(int(top_left_square[0]) - 1) + str(int(top_left_square[1]) - 1)) #sets the square to the top left square of the king

    for row in range(top_left_square[1],top_left_square[0] + 3): #repeats 3 times for each row
        for column in range(top_left_square[0],top_left_square[0] + 3): #scans a 3x3 area around the king
            current_square = column + row
            if squares_in_board([current_square]) == [current_square]: #means square is part of board
                if colour == 'White':
                    if check_piece_at_square(current_square,board) not in white_pieces:
                        possible_squares.append(current_square)
                else:
                    if check_piece_at_square(current_square,board) not in black_pieces:
                        possible_squares.append(current_square)
    #add all the squares around the king
    #remove all the squares outside the board
    #remove all the squares occupied by the piece of the same colour
    test(possible_squares)
    return possible_squares
'''Finish subroutines above here.'''
def setup_players():
    '''Gets the names of each player'''
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
    #cool_coloured_text('/mhello/cnew')
    menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    while menu_result not in ['1', '2']:
        #clear() TESTING ONLY! REMOVE # WHEN COMPLETE
        menu_result = input('Welcome to Chess 960!\n1. Open instructions\n2. Start new game\nEnter what you want to do: ')
    return menu_result

def capture_own_check(end,board,colour):
    '''Checks if a move ends on a piece of the same colour.'''
    if colour == 'White':
        if check_piece_at_square(end,board) in white_pieces:
            return False
            
        else:
            return True
    else:
        if check_piece_at_square(end,board) in black_pieces:
            return False
        else:
            return True

def no_move_check(start,end):
    '''Checks if the starting square is the same as the ending square.'''
    if start == end:
        return False
    else:
        return True

def opposite_turn_movement(start,board,colour):
    '''Returns false if a piece is selected on the opponent's turn'''
    if check_piece_at_square(start,board) in black_pieces and colour == 'White': #selecting black piece during white turn
        return False
    elif check_piece_at_square(start,board) in white_pieces and colour == 'Black': #selecting white piece during black turn
        return False
    else:
        return True
    
def king_conditions(start,end,board,colour):
    '''Returns true if the king move is legal'''
    #needs to make an incheck() and checkmate() functions first
    pass

def queen_conditions(start,end,board,colour):
    '''Returns true if the queen move is legal'''
    if rook_conditions(start,end,board,colour) or bishop_conditions(start,end,board,colour):
        return True
    else:
        return False
    
def pawn_conditions(start,end,board,colour):
    '''Returns true if the pawn move is legal'''
    #cant capture own pieces
    if colour == 'White':
        test('Pawn is white')
        if start[0] == end[0]: #same column
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

        if start[0] == end[0]:
            test('column is the same')
            pieces, _ = pieces_in_between(start,end,'vertical',board)
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
    '''Returns true if the knight move is legal'''
    start_column, start_row = start #multi variable assignment
    end_column, end_row = end
    start_row, end_row = int(start_row), int(end_row)
    
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
    '''Returns true if the rook move is legal'''
    # Check for vertical movement
    if start[0] == end[0]:  # Same column
        pieces, direction = pieces_in_between(start, end, 'vertical', board)
        test(pieces)
        # Ensure all pieces between the start and end are empty
        if len(pieces) != 0: #len 0 needs special case
            for piece in pieces:
                if piece != '.': #if the square is not empty
                    return False  # Blocked by another piece
        else:
            if check_piece_at_square(end,board) == '.':
                test('end is empty')
                return True
        if move_limits(pieces,direction,start,end,colour) == True:
            return True
        else:
            return False

    # Check for horizontal movement
    elif start[1] == end[1]:  # Same row
        pieces, direction = pieces_in_between(start, end, 'horizontal', board)
        test(pieces)
        # Ensure all pieces between the start and end are empty
        if len(pieces) != 0: #len 1 needs special case (moving 1 square past)
            for piece in pieces:
                if piece != '.': #if the square is not empty
                    return False  # Blocked by another piece
        else:
            if check_piece_at_square(end,board) == '.':
                test('end is empty')
                return True
            
        if move_limits(pieces,direction,start,end,colour) == True:
            return True
        else:
            return False
    
    return False  #invalid move (not straight)

def bishop_conditions(start,end,board,colour):
    '''Returns true if the bishop move is legal'''
    #setup direction and pieces
    direction = pieces_in_between(start,end,'diagonal',board)
    pieces = []

    start_column, start_row = turn_notation_compatible(start)
    start_column_int, start_row_int = int(start_column), int(start_row)
    #generate a list of all possible moves for 4 cases
    possible_end_squares = [] 
    #case 1: diagonal, up, right
    for _ in range(8): #since bishops can move furthest, 8 squares in a specific direction
        start_column = str(int(start_column) + 1) #right
        start_row = str(int(start_row) - 1) #up #inverted row scale, high notation row = low row
        current_square = start_column + start_row

        if len(current_square) == 2:
            test(f'case 1 {reverse_notation(current_square)}')
            possible_end_squares.append(reverse_notation(current_square))  #adds the square 1 up and 1 right of the previous
            if direction == 'upright' and [reverse_notation(current_square)] == squares_in_board(current_square): #if square is in the board and moving upright
                pieces.append(check_piece_at_square(reverse_notation(current_square)))
    
        # Case 2: diagonal, up, left
    temp_column = start_column_int
    temp_row = start_row_int
    for _ in range(8):
        temp_column -= 1  # left
        temp_row -= 1     # up (inverted row scale)
        current_square = str(temp_column) + str(temp_row)
        if len(current_square) == 2:  # This now works correctly because temp_row is int, no negative sign
            test(f'case 2 {reverse_notation(current_square)}')
            possible_end_squares.append(reverse_notation(current_square))
            if direction == 'upleft' and [reverse_notation(current_square)] == squares_in_board(current_square):
                pieces.append(check_piece_at_square(reverse_notation(current_square)))

    # Case 3: diagonal, down, right
    temp_column = start_column_int
    temp_row = start_row_int
    for _ in range(8):
        temp_column += 1  # right
        temp_row += 1     # down
        current_square = str(temp_column) + str(temp_row)
        if len(current_square) == 2:
            test(f'case 3 {reverse_notation(current_square)}')
            possible_end_squares.append(reverse_notation(current_square))
            if direction == 'bottomright' and [reverse_notation(current_square)] == squares_in_board(current_square):
                pieces.append(check_piece_at_square(reverse_notation(current_square)))
            
    #case 4: diagonal, down, left
    for _ in range(8): 
        start_column = str(int(start_column) - 1) #left
        start_row = str(int(start_row) + 1) #down  #inverted row scale, high notation row = low row
        current_square = start_column + start_row
        
        if len(current_square) == 2:
            test(f'case 4 {reverse_notation(current_square)}')
            possible_end_squares.append(reverse_notation(current_square)) 
            if direction == 'bottomleft' and [reverse_notation(current_square)] == squares_in_board(current_square): #if square is in the board and moving upright
                pieces.append(check_piece_at_square(reverse_notation(current_square)))

    possible_end_squares = squares_in_board(possible_end_squares) #only gets the squares inside the board
    test(possible_end_squares)
    for index in range(len(possible_end_squares)):
        possible_end_squares[index] = possible_end_squares[index][0] + str(possible_end_squares[index][1])
    test(possible_end_squares)
    if end in possible_end_squares: #if the end square is in the list of all possible squares
        for piece in pieces:
            if piece != '.':
                return False #not empty squares in between
        return True
    else:
        return False #if the end square is not within bishop scope and moves
    
def squares_in_board(list_of_squares):
    '''Checks if squares are part of the board. Returns a list of squares only part of the board.'''
    new_list_squares = []
    for square in list_of_squares:
        if square[0] in ['a','b','c','d','e','f','g','h'] and square[1] in [1,2,3,4,5,6,7,8]:
            new_list_squares.append(square)
    return new_list_squares

def pieces_in_between(start, end, mode, board):
    '''Returns the list of pieces in between 2 squares, depending on the mode. Also returns the direction from start to end.'''
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
        # 4 cases
        start_column, start_row = turn_notation_compatible(start) #notation is (11) example
        end_column, end_row = turn_notation_compatible(end) #notation is (12) example

        if end_column > start_column and end_row < start_row: #top right, as row scale is inverted
            direction = 'upright'
        elif end_column < start_column and end_row < start_row: #top left
            direction = 'upleft'
        elif end_column > start_column and end_row > start_row: #bottom right
            direction = 'bottomright'
        elif end_column < start_column and end_row > start_row: #bottom left
            direction = 'bottomleft'
        else:
            direction = None
        return direction #returns direction only, instead of pieces and direction
    return [pieces_between,direction]  #return pieces in between
    

def move_limits(pieces_in_between, direction, start_square, end_square, colour):
    '''Finds the furthest square to move to, based on the direction of movement and the square the user wants to move from and to.'''
    black_pieces = ['♔', '♕', '♖', '♖', '♗', '♗', '♘', '♘','♙']
    white_pieces = ['♚', '♛', '♜', '♜', '♝', '♝', '♞', '♞','♟']
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
        furthest_square = int(str(start[0]) + str(start[1] + furthest)) #error 
        print(f'TEST: {furthest_square} and {turn_notation_compatible(furthest_square)} and {reverse_notation(furthest_square)}') #TESTING ONLY
        furthest_square = reverse_notation(furthest_square)
        if int(end_square[1]) > furthest_square[1]:
            print(f'You cannot move to {end_square}. The furthest you can move to with that piece is {furthest_square}')
            return False
        else:
            return True
        
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

    print(f'When you tried to move from {start_square} to {end_square}, the furthest you could move to was {furthest_square}') #TESTING
    



def turn_notation_compatible(square):
    '''Turns the notation in chess format (a4) into an indexable format (04)'''
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