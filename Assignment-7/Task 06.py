import heapq
from collections import defaultdict

def second_shortest_path(n, m, s, d, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))


    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[s][0] = 0
    pq = [(0, s)]  # (current_distance, current_node)

    while pq:
        cost, u = heapq.heappop(pq)
        for v, w in graph[u]:
            new_cost = cost + w


            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(pq, (new_cost, v))

            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return dist[d][1] if dist[d][1] != float('inf') else -1

def main():
    n, m, s, d = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(second_shortest_path(n, m, s, d, edges))

main()
