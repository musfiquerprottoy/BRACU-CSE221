import sys
input = sys.stdin.readline


n= int(input())
for _ in range(n):
    #t = sys.stdin.read().splitlines()
    t = int(input())
    if t%2==0:
        print(f'{t} is an Even number.')
    else:
        print(f'{t} is an Odd number.')
