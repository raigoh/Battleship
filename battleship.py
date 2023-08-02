# Import randint function from random module
# from random import randint
import random

length_of_ships = [2,3,3,4,5]
hidden_pattern = [[' ']*8 for i in range(8)]
guess_pattern = [[' ']*8 for i in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
board = []


# for x in range(8):
#     board.append(['|'] * 8)

# Function is defined to print the board of battleship
def build_board(board):
    print('  A B C D E F G H')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# build_board(board)


def user_guess():
    # Enter the row number between 1 to 8
    row = input('Row: ')
    while row not in '12345678':
        print("Please enter a valid row number! (1-8)")
        row = input('Row: ')
        # Enter the Ship column from A TO H
    column = input('Column: ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column letter! (A-H)")
        column = input('Column: ').upper()
    return int(row) - 1, let_to_num[column]


# user_guess()

# Function that creates the ships
def build_ships(board):
    # loop through length of ships
    # length_of_ships = [2,3,3,4,5]
    for ship_length in length_of_ships:
        # loop until ship fits and doesn't overlap
        while True:
            if board == hidden_pattern:
                orientation, row, column = random.choice(
                    ["H", "V"]), random.randint(0, len(board) -1), random.randint(0, len(board) -1)
                if check_ship_fit(ship_length, row, column, orientation):
                    # check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        # place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
                    
# check if ship fits in board
def check_ship_fit(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True

# check each position for overlap
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

# def build_ships(board):
    # for ship in range(5):
    #     ship_r, ship_cl = random.randint(0, len(board) -1), random.randint(0, len(board) -1)
    #     while board[ship_r][ship_cl] == 'X':
    #         ship_r, ship_cl = random.randint(0, len(board) -1), random.randint(0, len(board) -1)
    #     board[ship_r][ship_cl] = 'X'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def welcome_message():
    print('Welcome to Battleship!')
    print('There is 5 hidden battleships in this board. One carrier (5 holes), one battleship (4 holes), one destroyer (3 holes), one submarine (3 holes) and one patrol boat (2 holes). Enter your row and column guesses to sink it!')


welcome_message()


build_ships(hidden_pattern)
turns = 25
while turns > 0:
    build_board(guess_pattern)
    row, column = user_guess()
    if guess_pattern[row][column] == '-' or guess_pattern[row][column] == 'X':
        print('You already guessed that')
    elif hidden_pattern[row][column] == 'X':
        print('Congratulations you have hit the battleship')
        guess_pattern[row][column] = 'X'
        # turns -= 1
    else:
        print('Sorry,You missed')
        guess_pattern[row][column] = '-'
        turns -= 1
    if count_hit_ships(guess_pattern) == 17:
        print("Congratulations you have sunk all the battleships")
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Game Over')
        break
