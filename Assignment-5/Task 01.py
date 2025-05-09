from collections import deque, defaultdict

n, m = map(int, input().split())
adj = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for key in adj:
    adj[key].sort()

visited = [False] * (n+1)
output = []
queue = deque([1])
visited[1] = True


while queue:
    node = queue.popleft()
    output.append(node)
    for neighbour in adj[node]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)
print(*output)