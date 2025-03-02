def bubbleSort(arr):
    n = len(arr)
    swapped = True 
    i = 0

    while swapped:
        swapped = False
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        i += 1  

arr = [2, 3, 54, 76, 1, 4]
bubbleSort(arr)
print(arr)
