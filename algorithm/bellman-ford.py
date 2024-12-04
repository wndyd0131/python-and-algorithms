INF = float('inf')

node_num = 7

graph = [[0, 6, 5, 5, INF, INF, INF],
         [INF, 0, INF, INF, -1, INF, INF],
         [INF, -2, 0, INF, 1, INF, INF, INF],
         [INF, INF, -2, 0, INF, -1, INF],
         [INF, INF, INF, INF, 0, INF, 3],
         [INF, INF, INF, INF, INF, 0, 3],
         [INF, INF, INF, INF, INF, INF, 0]]

edge_list = [(1,2), (1,3), (1,4), (2,5), (3,2), (3,5), (4,3), (4,6), (5,7), (6,7)]

d = [INF for _ in range(node_num)]

def bellman_ford(start):
    d[start] = 0
    for i in range(node_num-1):
        # relaxation # if (d[u] + graph[u][v] < d[v]) d[v] = d[u] + graph[u][v]
        for u,v in edge_list:
            u, v = u - 1, v - 1
            if d[u] + graph[u][v] < d[v]:
                d[v] = d[u] + graph[u][v]
    for u,v in edge_list:
        u, v = u - 1, v - 1
        if d[u] + graph[u][v] < d[v]:
            print("no solution")


bellman_ford(0)
for i in d:
    print(i)