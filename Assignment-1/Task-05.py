def bubbleSort(arr, n):                                                 
    for i in range(n - 1):
        swapped = False  # Track if any swaps occur in this pass
        
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True  # Swap happened, so continue sorting
        
        if not swapped:  # If no swaps occurred, array is already sorted
            break  

# Taking input
N = int(input())  # Read array size
arr = list(map(int, input().split()))  # Read array elements

bubbleSort(arr, N)  # Sort the array

# Print the sorted array
print(*arr)
