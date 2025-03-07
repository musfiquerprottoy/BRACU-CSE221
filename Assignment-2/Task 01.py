N, target_sum = map(int, input().split())
arr = list(map(int, input().split()))

def two_sum(arr, target_sum): 
    one = 1
    two = len(arr)

    while one<two: 
        current_sum = arr[one-1] + arr[two-1]

        if current_sum == target_sum: 
            return (one, two)
        elif current_sum < target_sum: 
            one +=1
        else: 
            two -=1
    return 

result = two_sum(arr, target_sum)
if result: 
    print(*result)
else: 
    print(-1)
