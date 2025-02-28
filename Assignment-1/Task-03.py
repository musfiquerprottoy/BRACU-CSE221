import numpy as np
n = int(input())
k = int(input())
arr = np.zeros(n, dtype=int)
for i in range(n): 
    arr[i] = int(input())
arr2 = np.zeros(n, dtype=int)
num = 0
for i in range(arr.size-1, -1, -1):
    arr2[num] = arr[i]
    num += 1  
print(arr2[n-k:])
