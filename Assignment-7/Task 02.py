import heapq
import sys

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d+w:
                dist[v] = d+w
                heapq.heappush(pq, (dist[v], v))
    return dist


def solve():
    n, m, s, t = map(int, input().split())
    '''
        n = Number of verticies
        m = Number of edges
        s = Starting node Alice
        t = starting node Bob
    '''
    if s == t:
        print(f'0 {s}')
        return
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dist_from_s = dijkstra(n, graph, s)
    dist_from_t = dijkstra(n, graph, t)

    min_time = float('inf')
    meeting_node = -1

    for node in range(1, n+1):
        ds = dist_from_s[node]
        dt = dist_from_t[node]
        if ds == float('inf') or dt == float('inf'):
            continue
        current_max = max(ds, dt)
        if current_max < min_time or (current_max == min_time and node<meeting_node):
            min_time = current_max
            meeting_node = node
            meeting_node = node
    if meeting_node == -1:
        print(-1)
    else:
        print(min_time, meeting_node)
solve()