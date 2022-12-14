from random import randrange, random
from random import choice
rc1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
moves = []

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", rc1[0][0], "  |  ", rc1[0][1], "  |  ", rc1[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", rc1[1][0], "  |  ", rc1[1][1], "  |  ", rc1[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", rc1[2][0], "  |  ", rc1[2][1], "  |  ", rc1[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(rc1):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    try:
        hm = int(input("Enter you move : "))

        if hm > 0 and 10 > hm  and hm != '' and hm in moves:                      # Check if same move already made by user
           hm = int(input("Another number, please: "))
           moves.append(hm)
        else:
             moves.append(hm)
    except ValueError:
        hm = int(input("Enter you move : "))
    except:
        hm = int(input("Enter you move : "))

    print("-->",moves,"<--")

    for z in rc1:                               # iterating through rows
            for w in range(len(z)):             # iterating through columns
                if z[w] == hm and z[w] != 'O' and z[w] != 'X': # check if square is free
                    z[w] = 'O'                  # claim with 'O'

    return rc1

def make_list_of_free_fields(rc1):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_board = []
    free_board_2 = []
    global c
    c = 9

    for z in rc1:
        for w in range(len(z)):
            free_board_2.append(z[w])                           # Creating a list with values from board after moves

    for g in range(len(rc1)):
        for y in range(len(rc1)):
            t = g, y
            free_board.append(t)                                # Creating list with tuples (row, column)

    for j in range(len(free_board_2) - 1, -1, -1):              # Going back in list, because of index error
        if free_board_2[j] == 'X' or free_board_2[j] == 'O':    # Both lists are the same length,
                                                                # iterating through first list and deleting same index in second list
            free_board.remove(free_board[j])
            c -= 1                                              # quantati of free fields - uses in victory function for tie definition

def victory_for(rc1, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
        global res
        res = True
        r1 = []
        r2 = []
        r3 = []
        for j in rc1[0]:                                         # splitting list in lists like rows for value compare
            r1.append(j)
        for k in rc1[1]:
            r2.append(k)
        for l in rc1[2]:
            r3.append(l)
        if r1[0] == r2[0] == r3[0] == 'X' or \
                r1[0] == r2[1] == r3[2] == 'X' or \
                r1[0] == r1[1] == r1[2] == 'X'or \
                r2[0] == r2[1] == r2[2] == 'X'or \
                r3[0] == r2[1] == r1[2] == 'X'or \
                r1[2] == r2[2] == r3[2] == 'X'or \
                r1[1] == r2[1] == r3[1] == 'X'or \
                r3[0] == r3[1] == r3[2] == 'X':
            print('X Victory')
            res =  False
            return res
        elif r1[0] == r2[0] == r3[0] == 'O' or \
                r1[0] == r2[1] == r3[2] == 'O' or \
                r1[0] == r1[1] == r1[2] == 'O'or \
                r2[0] == r2[1] == r2[2] == 'O'or \
                r3[0] == r2[1] == r1[2] == 'O'or \
                r1[2] == r2[2] == r3[2] == 'O'or \
                r1[1] == r2[1] == r3[1] == 'O'or \
                r3[0] == r3[1] == r3[2] == 'O':
            print(sign + ' is Victory')
            res =  False
            return res
        elif c < 1:
            print("Tie")
            res = False
            return res
        else:
            res = True
            return res
        return res


def draw_move(board):
    # The function draws the computer's move and updates the board.
    import random
    cm = 5

    if cm not in moves:  # Check if same move already made by random generator
        moves.append(cm)
    elif cm in moves:

        all_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_list = [x for x in all_squares if x not in moves] # makes a new list without ocuppied squares
        cm = random.choice(new_list)                          # picks random number
        moves.append(cm)

    print("+++<", moves, ">+++")

    for t in rc1:  # iterating through rows
        for y in range(len(t)):  # iterating through columns
            if t[y] == cm and t[y] != 'X' and t[y] != 'O':  # check if square is free
                t[y] = 'X'  # claim with 'X'

    return rc1
    print(rc1)

while True:

    draw_move(rc1)
    make_list_of_free_fields(rc1)
    victory_for(rc1, 'O')
    display_board(rc1)
    if res != True:
        break

    enter_move(rc1)
    make_list_of_free_fields(rc1)
    victory_for(rc1, 'O')
    display_board(rc1)
    if res != True:
        break
