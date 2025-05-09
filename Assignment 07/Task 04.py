import heapq


def dijkstra(n, graph, node_weights, start, end):
    dist = [float('inf')] * (n + 1)
    dist[start] = node_weights[start - 1]  # Start node includes its weight
    pq = [(node_weights[start - 1], start)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_node == end:
            return current_cost


        for neighbor in graph[current_node]:
            new_cost = current_cost + node_weights[neighbor - 1]
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return -1


def solve():
    n, m, s, d = map(int, input().split())  # n = nodes, m = edges, s = start, d = destination
    node_weights = list(map(int, input().split()))  # Weights of each node


    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)


    min_cost = dijkstra(n, graph, node_weights, s, d)
    print(min_cost)
solve()
