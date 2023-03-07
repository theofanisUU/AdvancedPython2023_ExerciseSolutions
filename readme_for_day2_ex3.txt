For exercise 3a
matmult blocks were changed to functions and using the cprofiler we see that
the performance impedence seems to come from the multiplication of the matrices



For exercise 3b
The c profiler points most of time allocated to the "factorize" part
The line profiler confirms the above statement focussing on lines:
    25     96347      30773.7      0.3     20.3      for p in primes:
    26     96347      39674.2      0.4     26.2          while(n%p == 0):
    29     86348      41186.9      0.5     27.2          if(p > sqrt(n)):
Notes:
1) A common thing in all those lines is that they are accessing p variable in the list
2) Sqrt of the fixed n variable is needlessly calculated at each loop iteration



For exercise 3c
line profiler verifies what we saw in 3a focusing the issues on:
Total time: 16.5312 s
Function: multiply at line 28
35  15687500    4943168.4      0.3     29.9      for k in range(len(Y)):
36  15687500   11568357.2      0.7     70.0          result[i][j] += X[i][k] * Y[k][j]

proposed solutions:
1) calculate lengths and ranges once
2) create an easily accessible temporary variable to store calculated Rij elemnt in the new matrix
and then set the value of the result[i][j] equal to the temporary
Total time: 15.3153 s
    33         1          0.4      0.4      0.0      ly=len(Y)
    34         1          0.5      0.5      0.0      ry=range(ly)
    41  15687500    5219095.2      0.3     34.1              for k in ry:
    42  15687500   10020928.6      0.6     65.4                  temp+= X[i][k] * Y[k][j]
    43     62750      31309.5      0.5      0.2              result[i][j] =temp
Solution 2 improved the performance much more than solution 1, so len() and range() are not impeding the performance significantly

3) constantly accesing X and Y still impedes perfromance, we can store the Xrow
in a temp list and access that instead of the much larger X list
Total time: 14.198 s
    27         1          3.4      3.4      0.0      ranX = range(len(X))
    28         1          1.0      1.0      0.0      ranY0 = range(len(Y[0]))
    29         1          0.5      0.5      0.0      ranY=range(len(Y))
    30                                               # iterate through rows of X
    31       250         77.6      0.3      0.0      for i in ranX:
    32                                                   # iterate through columns of Y
    33     62750      23318.8      0.4      0.2          for j in ranY0:
    34                                                       # iterate through rows of Y
    35     62750      21113.3      0.3      0.1              tempRes=0
    36     62750      24772.6      0.4      0.2              tempXrow= X[i]
    37  15687500    5086127.1      0.3     35.8              for k in ranY:
    38  15687500    9011430.0      0.6     63.5                  tempRes+= tempXrow[k] * Y[k][j]
    39
    40     62750      31139.5      0.5      0.2              result[i][j] = tempRes

The performance was improved again!


The optimised script can be found in the repo with the name matmult_opy.py



