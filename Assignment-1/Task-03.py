import numpy as np

N = int(input())
K = int(input())

arr = np.zeros(N, dtype=int)

for i in range(N): 
    arr[i] = int(input())

arr2 = arr[::-1]
print(*arr2[N-K:])