
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    text = input().strip()
    final = text.replace('calculate', '').strip()
    result = eval(final)
    print(f'{result:.6f}')
