boardTemplate = '''
 {} │ {} │ {}
───┼───┼───
 {} │ {} │ {}
───┼───┼───
 {} │ {} │ {}
'''

def updateBoard(board):
    print(boardTemplate.format(*board))

def askPlayer(board):
    userInput = input('\nchoose [1-9]: ')
    if userInput.isdigit() and 1 <= int(userInput) <= 9 and board[int(userInput)-1] == '_': # intCheck; between 1-9; notTaken
        return int(userInput)
    else:
        print('- Choose a nuber between 1 and 9 that is not already taken -')
        return askPlayer(board)

# most powerfull code ever!
def checkWin(board, symbol):
    booleans = []
    for i in range(3):
        start = i*3
        booleans.append(all(v == symbol for v in board[start:start+3])) # symbols in row; True/False
        booleans.append(all(v == symbol for v in board[i::3])) # symbols in colmn; True/False
    booleans.append(all(v == symbol for v in board[::4])) # symbols in diagonal (1, 5, 9); True/False
    booleans.append(all(v == symbol for v in board[2::2][:3])) # symbols in diagonal (3, 5, 7); True/False
    return True in booleans # if booleans contain True: True; else: False
