#script to test numpy functionalities
#ALL ANSWERS ARE AUTO PRINTED ON RUN

import numpy as np


# a. Create a null vector of size 10 but the fifth value which is 1
a=np.zeros(10)
a[4]=1
print(f"{a}",end="\n\n")

# b. Create a vector with values ranging from 10 to 49
b = np.arange(10,50,1)
print(f"{b}",end="\n\n")

# c. Reverse a vector (first element becomes last)
c=b[::-1]
print(f"{c}",end="\n\n")

# d. Create a 3x3 matrix with values ranging from 0 to 8
d=np.arange(0,9,1)
d = d.reshape(3,3)
print(f"{d}",end="\n\n")

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
e_init=np.array([1,2,0,0,4,0])
e=e_init.nonzero()[0]
print(f"Array: {e_init} non zero Indices: {e}",end="\n\n")

# f. Create a random vector of size 30 and find the mean value
f=np.random.rand(30)
print(f"mean of 30 rand values: {np.mean(f)}",end="\n\n")

# g. Create a 2d array with 1 on the border and 0 inside
g = np.zeros(64).reshape(8,8)
g[0,:]=1
g[7,:]=1
g[:,0]=1
g[:,7]=1
print(f"{g}",end="\n\n")

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
h_1=[0,1, 0, 1, 0, 1, 0, 1]
h_2=[1, 0, 1, 0, 1, 0, 1,0]
h=np.array([h_1,h_2,h_1,h_2,h_1,h_2,h_1,h_2])
print(f"{h}",end="\n\n")

# i. Create a checkerboard 8x8 matrix using the tile function
i= np.array([[0,1],[1,0]])
i_2=np.tile(i,(4,4))
print(f"{i_2}",end="\n\n")

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
j = np.arange(12)
j_b= np.logical_or(j<3,j>8 )
print(j_b);print(j[j_b],end="\n\n")

#k. Create a random vector of size 10 and sort it
k_u = np.random.random(10)
k = np.sort(k_u)
print(f"unsorted: {k_u}\nsorted {k}",end="\n\n")

#l. Consider two random array A anb B, check if they are equal
l1 = np.random.randint(0,2,5)
l2 = np.random.randint(0,2,5)
print(f"l1: {l1}\nl2: {l2}\nEqual arrays: {np.array_equal(l1,l2)}",end="\n\n")


#m. How to convert an integer (32 bits) array into a float (32 bits) in place?
m = np.arange(10, dtype=np.int32)
m2 = np.array(m,dtype=np.float32)
print(m,m.dtype)
print(m2,m2.dtype,end="\n\n")

#n. How to get the diagonal of a dot product?
n_a = np.arange(9).reshape(3,3)
n_b = n_a + 1
n_dot = np.dot(n_a,n_b)
print(n_dot)
for i in range(0,3):
    print(f"{n_dot[i,i]}")

