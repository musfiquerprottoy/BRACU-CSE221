n = int(input())
arr = list(map(int, input().split()))

unsorted_term = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i]>arr[j]:
            unsorted_term += 1
if unsorted_term%2==0:
    print("YES")
else:
    print("NO")
