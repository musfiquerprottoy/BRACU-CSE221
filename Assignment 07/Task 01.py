import heapq

# Read input
n, m, s, d = map(int, input().split())
'''
    n = Number of nodes
    m = number of edges
    s = source node
    d = destination node 
'''
u = list(map(int, input().split())) # Nodes
v = list(map(int, input().split())) # Nodes
w = list(map(int, input().split())) # weights

def dijkstra(graph, s, d):
    if not graph:
        return -1, []
    dist = [float('inf')] * (n + 1)
    prev = [None] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        curr_dist, curr = heapq.heappop(pq)
        if curr == d:
            break
        if curr_dist > dist[curr]:
            continue
        for neighbor, weight in graph[curr]:
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = curr
                heapq.heappush(pq, (distance, neighbor))

    if dist[d] == float('inf'):
        return -1, []

    # Reconstruct path
    path = []
    current = d
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return dist[d], path


graph = [[] for _ in range(n + 1)]
for i in range(m):
    graph[u[i]].append((v[i], w[i]))
distance, path = dijkstra(graph, s, d)

if distance == -1:
    print(-1)
else:
    print(distance)
    print(' '.join(map(str, path)))