num = int(input())
arr = list(map(int, input().split()))

n = len(arr)
swapped = True 

while swapped: 
    swapped = False 
    for i in range (n-1): 
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1] , arr[i]
            swapped = True 

print(" ".join((map(str, arr))))