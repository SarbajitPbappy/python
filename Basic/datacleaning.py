import heapq
nodes,edges=map(int , input().split())
d=[float('inf')*(nodes+1)]
visited=[0]*(nodes+1)
adj_list=[[]for _ in range(nodes+1)]
def dijkstra(src):
    d[src]=0
    pq = [(0,src)]
    while pq:
        dist,vertex=heapq.heappop(pq)
        if visited[vertex]:
            continue
        visited[vertex]=1
        for v,w in adj_list[vertex]:
            if dist+w<d[v]:
                d[v]=dist+w
                heapq.heappush(pq,(d[v],v))
for _ in range(edges):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
for i in range(1,nodes+1):
    print(d[i],end=" ")
print()