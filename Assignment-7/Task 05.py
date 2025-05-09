import heapq
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(m):
        graph[u[i]].append((v[i], w[i]))

    dist = [[float('inf')] * 2 for _ in range(n + 1)]  # dist[node][parity]
    dist[1][0] = 0
    dist[1][1] = 0
    pq = [(0, 1, -1)]  # (distance, node, previous_parity)

    while pq:
        d, u, prev_parity = heapq.heappop(pq)

        for v, wght in graph[u]:
            parity = wght % 2
            if parity == prev_parity:
                continue

            if d + wght < dist[v][parity]:
                dist[v][parity] = d + wght
                heapq.heappush(pq, (d + wght, v, parity))

    res = min(dist[n][0], dist[n][1])
    print(res if res != float('inf') else -1)

solve()
