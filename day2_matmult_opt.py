# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
X = []
def fillX():
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
fillX()

# Nx(N+1) matrix
Y = []
def fillY():
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
fillY()        

# result is N x(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

@profile
def multiply():
    ranX = range(len(X))
    ranY0 = range(len(Y[0]))
    ranY=range(len(Y))
    # iterate through rows of X
    for i in ranX:
        # iterate through columns of Y
        for j in ranY0:
            # iterate through rows of Y
            tempRes=0
            tempXrow= X[i]
            for k in ranY:
                tempRes+= tempXrow[k] * Y[k][j]
                
            result[i][j] = tempRes
            

multiply()

@profile
def printResult():
    for r in result:
        print(r)
   
printResult()
