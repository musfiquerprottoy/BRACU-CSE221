T = int(input())
for i in range(T): 
    N = int(input())
    if -10**5 <= N <= 10**5: 
        if N%2 == 0: 
            print(f'{N} is an Even number.')
        else: 
            print(f'{N} is an Odd number.')
    else: 
        break 