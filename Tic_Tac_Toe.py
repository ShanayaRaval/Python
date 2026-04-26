'''We will make the board using ditionary
   in which keys will be the location (i.e : top - left, mid - right, etc.) 
   and initially it's values will be empty space and then after every move
   we will change the value according to the player's choice of move.'''

theBoard = {'7' : '', '8' : '', '9' : '',
            '4' : '', '5' : '', '6' : '',
            '1' : '', '2' : '', '3' : ''}

Board_keys = []

for key in theBoard:
    Board_keys.append(key)

'''We will have to print the appended boar after every move and
   thus we will make a function in which we'll define the printBoard function
   so that we can easily print the board every time by calling this function.'''

def printBoard(Board):
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])
    print('--+--+--')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('--+--+--')
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, ", turn, " .Move to which place?")

        move = input()

        if theBoard[move] == '':
            theBoard[move] = turn
            count += 1

        else:
            print("That plce is already filled. Move to which place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '':
                printBoard(theBoard)
                print("\n Game Over!\n")
                print("****" + turn + "won***")

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '':
                printBoard(theBoard)
                print("\n Game Over!\n")
                print("****" + turn + "won***")

            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != '':
                printBoard(theBoard)
                print("\n Game Over!\n")
                print("****" + turn + "won***")

            elif theBoard[''] == theBoard['5'] == theBoard['6'] != '':
                printBoard(theBoard)
                print("\n Game Over!\n")
                print("****" + turn + "won***")

