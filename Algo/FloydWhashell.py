INF = float('inf')

def shortest_path(n, graph, queries):
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n + 1):
                if dist[k][j] == INF:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for q1, q2 in queries:
        if dist[q1][q2] == INF:
            print(-1)
        else:
            print(dist[q1][q2])

# Read the input
cities, roads, qn = map(int, input().split())
graph = []
for _ in range(roads):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))
queries = []
for _ in range(qn):
    q1, q2 = map(int, input().split())
    queries.append((q1, q2))

# Solve the problem
shortest_path(cities, graph, queries)
