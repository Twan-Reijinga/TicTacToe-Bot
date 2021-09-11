# eval means evaluation
from gameBoard import checkWin

def getBestMove(board, symbol):
    if symbol == 'o':
        nextSymbol = 'x'
    else:
        nextSymbol = 'o'
    evalIndexes = []
    allMoves = getAllPossibleMoves(board, symbol)
    for move in allMoves:
        if checkWin(move, symbol):
            evalIndex = 1
        else:
            evalIndex = getEvalIndex(move, nextSymbol)/-1
        evalIndexes.append(evalIndex)
    maxEvalIndex = max(evalIndexes)
    bestPos = evalIndexes.index(maxEvalIndex)
    bestMove = getBoardPos(bestPos, board)
    return bestMove

def getEvalIndex(board, symbol):
    if symbol == 'o':
        nextSymbol = 'x'
    else:
        nextSymbol = 'o'
    
    allMoves = getAllPossibleMoves(board, symbol)
    if (len(allMoves) == 0):
        return 0
    evalIndexes = []
    for board in allMoves:
        if checkWin(board, symbol):
            evalIndex = 1
        else:
            evalIndex = getEvalIndex(board, nextSymbol)/-1
        evalIndexes.append(evalIndex)
    return max(evalIndexes)
        
def getAllPossibleMoves(board, symbol):
    allMoves = []
    for i in range(len(board)):
        if board[i] == '_':
            board[i] = symbol
            allMoves.append(board.copy())
            board[i] = '_'
    return allMoves

def getBoardPos(bestPos, board):
    # best move calculates best move of the board that possible. 
    # If you make the move on the board you have to convert it to the boardPos.
    emptySpaces = 0
    
    for position in range(9):
        if board[position] == '_':
            
            emptySpaces += 1
        if emptySpaces == bestPos+1:
            return position # returns position of the bestMove
