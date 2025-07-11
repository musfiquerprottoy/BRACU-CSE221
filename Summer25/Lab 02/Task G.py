length, N = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(N):
    x, y = map(int, input().split())
    left = 0
    right = length
    while left<right:
        mid = (left+right)//2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    lower = left

    left = 0
    right = length
    while left<right:
        mid = (left + right) // 2
        if arr[mid] <= y:
            left = mid +1
        else:
            right = mid
    upper = left
    print(upper - lower)
