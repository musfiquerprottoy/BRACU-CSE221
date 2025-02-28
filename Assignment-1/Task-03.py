import numpy as np
N = int(input())
K = int(input())
arr = np.zeros(N, dtype=int)
for i in range(N): 
    arr[i] = int(input())
arr2 = np.zeros(N, dtype=int)
num = 0
for i in range(N-1, -1, -1):
    arr2[num] = arr[i]
    num += 1  
for j in range(N-K, N, 1): 
    print(arr2[j], end=' ')