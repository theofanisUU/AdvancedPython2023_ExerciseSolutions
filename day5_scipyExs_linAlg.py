import scipy
import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([1,2,3])

res = scipy.linalg.solve(A, b) #system raised warning for matrix A
print(res)
# testing solution
print(A.dot(res),end="\n\n") 

B = np.random.rand(9).reshape(3,3)

print("Random matrix check")
eigB = scipy.linalg.solve(B, b) #
eigenValues=eigB[0]
eigenVectors=eigB[1]
print(eigenValues)
print(eigenVectors)
# testing solution
print(B.dot(eigB),end="\n\n") #solution is accurate


detA = scipy.linalg.det(A) #determinant of A is zero, thats why solve raised the warning
print(f"determinant of A: {detA}",end="\n\n")

invA=scipy.linalg.inv(A) # thats why the inverse matrix does not make much sense
print(f"{invA}",end="\n\n")

eigA = scipy.linalg.eig(A)
print(f"eigen problem solution {eigA}",end="\n\n")

normA = scipy.linalg.norm(A)
print(f"norm of A {normA}",end="\n\n")
