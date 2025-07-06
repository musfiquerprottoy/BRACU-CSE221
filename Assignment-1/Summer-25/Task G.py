n = int(input())
ids = list(map(int, input().split()))
marks = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append((marks[i], ids[i], i))

arr.sort(key=lambda x: (-x[0], x[1]))

target_pos = [0] * n
for new_index in range(n):
    original_index = arr[new_index][2]
    target_pos[original_index] = new_index

visited = [False] * n
cycles = 0
for i in range(n):
    if not visited[i]:
        cycles += 1
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cur = target_pos[cur]

min_swaps = n - cycles
print(f"Minimum swaps: {min_swaps}")
for j in range(n):
    print(f"ID: {arr[j][1]} Mark: {arr[j][0]}")
