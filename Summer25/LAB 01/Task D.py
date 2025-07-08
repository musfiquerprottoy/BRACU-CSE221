import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int,input().split()))

    is_sorted = True
    for i in range(m-1):
        if arr[i] > arr[i+1]:
            is_sorted = False
            break
    print("YES" if is_sorted else "NO")
