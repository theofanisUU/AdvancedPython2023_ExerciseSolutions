# Program to multiply two matrices using nested loops
import random
import numpy as np

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


@profile
def multiply():
    npX=np.matrix(X)
    npY=np.matrix(Y)
    return npX*npY

result=multiply()   
print(result)
