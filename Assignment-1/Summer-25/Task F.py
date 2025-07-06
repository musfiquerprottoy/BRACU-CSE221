n = int(input())
arr = list(map(int, input().split()))

swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if (arr[i] % 2 == arr[i+1] % 2) and (arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True

print(*arr)
