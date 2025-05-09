from collections import defaultdict, deque
import sys
input = sys.stdin.read

def bfs(graph, S, par, dist):
    q = deque()
    dist[S] = 0
    q.append(S)

    while q:
        node = q.popleft()
        for neighbor in sorted(graph[node]):
            if dist[neighbor] == float('inf'):
                par[neighbor] = node
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

def print_shortest_distance(graph, S, D, V):
    par = [-1] * (V + 1)
    dist = [float('inf')] * (V + 1)

    bfs(graph, S, par, dist)

    if dist[D] == float('inf'):
        print(-1)
        return


    path = []
    current_node = D
    while current_node != -1:
        path.append(current_node)
        current_node = par[current_node]

    path.reverse()
    print(dist[D])
    print(*path)


data = input().split()
n, m, s, d = map(int, data[:4])
u = list(map(int, data[4:4 + m]))
v = list(map(int, data[4 + m:4 + 2 * m]))


graph = defaultdict(list)
for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

print_shortest_distance(graph, s, d, n)
