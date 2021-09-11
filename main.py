from gameBoard import updateBoard, askPlayer, checkWin
from algorithm import getBestMove

def main():
    board = ['_'] *9
    playerStarter = input('Do you want to start? [Y/n]: ')
    if playerStarter.lower() == 'n':
        playerStarter = False
    else:
        playerStarter = True
    for i in range(5):
        if playerStarter: 
            updateBoard(board)
            move = askPlayer(board) - 1
            board[move] = 'x'
        else:
            move = getBestMove(board, 'x')
            board[move] = 'x'
            updateBoard(board)

        if checkWin(board, 'x'):
            print('- x won -')
            updateBoard(board)
            break

        if (i < 4):
            if playerStarter: 
                move = getBestMove(board, 'o')
            else:
                move = askPlayer(board) - 1
            board[move] = 'o'

            if checkWin(board, 'o'):
                print('- O won -')
                updateBoard(board)
                break
        else:
            print('- it\'s a draw -')
            updateBoard(board)

main()
