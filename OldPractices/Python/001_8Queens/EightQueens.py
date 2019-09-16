# @Author: Ho Quang Thanh
import numpy as np
import timeit
from collections import deque

# Chess table size
size = 8

# Generate the init Chess table with 8 Queens
def generateInitChess():
    InitChessTable = [[0 for x in range(size)] for y in range(size)]
    for row in range(size):
        randInt = np.random.random_integers(0, 7)
        InitChessTable[row][randInt] = 1
    return list(InitChessTable)


# Print Chess table method
def printTable(table):
    tableString = ""
    for row in range(size):
        for col in range(size):
            tableString += "W " if table[row][col] else "- "
        tableString += "\n"
    print(tableString)

# Evaluation function: Col + Dia * 2
def evaluationFunc(table):
    evaluationValue = 0

    # Evaluate in each column
    for col in range(size):
        numW = 0
        for row in range(size):
            numW += 1 if table[row][col] else 0
        evaluationValue += numW - 1 if numW else 0

    # Evaluate in left-2-right diagonal
    for row in range(size):
        numW = 0
        rowT = row
        colT = 0
        while rowT < size:
            numW += 1 if table[rowT][colT] else 0
            colT += 1
            rowT += 1
        if numW: 
            evaluationValue += (numW - 1)*2

    col = 1
    while col < size:
        numW = 0
        rowT = 0
        colT = col
        while colT < size:
            numW += 1 if table[rowT][colT] else 0
            colT += 1
            rowT += 1
        evaluationValue += (numW - 1)*2 if numW else 0
        col += 1

    # Evaluate in right-2-left diagonal
    for row in range(size):
        numW = 0
        rowT = row
        colT = 0
        while rowT >= 0:
            numW += 1 if table[rowT][colT] else 0
            colT += 1
            rowT -= 1
        if numW: 
            evaluationValue += (numW - 1)*2

    col = 1
    while col < size:
        numW = 0
        rowT = size - 1
        colT = col
        while colT < size:
            numW += 1 if table[rowT][colT] else 0
            colT += 1
            rowT -= 1
        evaluationValue += (numW - 1)*2 if numW else 0
        col += 1
    return evaluationValue

# Travel in table
# Create the state
def forward(listC, num, size):
    a = num + 1
    if a == size:
        a = 0
    listC[num] = 0
    listC[a] = 1
    return listC

# Backtrack
def backward(listC, num, size):
    a = num - 1
    if a < 0: 
        a = size - 1
    listC[num] = 0
    listC[a] = 1
    return listC

def BFS(table):
    queue = deque([])
    for row in range(size):
        wNo = 0
        for col in range(size):
            if table[row][col]:
                wNo = col
                break
        eval = evaluationFunc(table)  
        queue.append(eval)      
        for _ in range(size - 1):
            table[row] = forward(table[row], wNo, size)
            evalT = evaluationFunc(table)
            if evalT < queue[0]:
                queue.popleft()
                queue.append(evalT)
            else:
                continue
                
    return table

# Solving the problem
InitChessTable = generateInitChess()
SolvingChess = InitChessTable

# Show the Initial Chess state
print("Initial Table:\n ")
printTable(InitChessTable)
print("Evalutate on Init chess: ",evaluationFunc(InitChessTable))

# Solving using BFS
start = timeit.default_timer()
# BFS
SolvedChess = BFS(SolvingChess)
stop = timeit.default_timer()
running_time = stop - start 

# Print
print("Solved Table:\n ")
printTable(SolvedChess)
print("Evalutate on Solved chess: ", evaluationFunc(SolvedChess))
print("Time: ",running_time)