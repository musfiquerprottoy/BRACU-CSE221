N, target_sum = map(int,input().split())
arr = list(map(int, input().split()))
found = False

starting = 1
ending = N

while starting < ending:
    current_sum = arr[starting-1] + arr[ending-1]
    if current_sum == target_sum:
        print(starting, ending)
        found = True
        break
    elif current_sum < target_sum:
        starting += 1
    else:
        ending -= 1
if not found:
    print(-1)
