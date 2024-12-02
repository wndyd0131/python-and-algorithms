import sys

def dfs(x, y, num):
    num += graph[x][y]

    if len(num) == 6:
        if num not in res:
            res.append(num)
        return
    
    for i in range(4):
        nr, nc = x + dr[i], y + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num)
    
res = []

graph = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(5):
    graph.append(list(sys.stdin.readline().split()))

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(res))