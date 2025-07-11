T = int(input())

for _ in range(T):
    k, x = map(int,input().split())
    left = 1
    right = 2*k
    while left<right:
        mid = (left+right)//2
        not_divisible = mid-(mid//x)

        if not_divisible<k:
            left = mid+1
        else:
            right = mid
    print(left)
