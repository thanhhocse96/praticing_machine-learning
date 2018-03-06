import numpy as np

#Chess table size
size = 8

def generateInitChess():
    InitChessTable = [[0 for x in range(size)] for y in range(size)]
    for row in range(size):
        randInt = np.random.randint(0, 8)
        InitChessTable[row][randInt] = 1
    return list(InitChessTable)

ChessTable = generateInitChess()
print (ChessTable)

