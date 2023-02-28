# N이하면 침수됨
# dfs, bfs

import sys
sys.setrecursionlimit(10 ** 6)

level = 0
mx = 0
cnt = 0
N = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
  for j in range(N):
    level = max(level, graph[i][j])

def dfs(r, c, n):
  visit[r][c] = True
  for i in range(4):
    nr, nc = r + dr[i], c + dc[i]
    if (0 <= nr < N and 0 <= nc < N) and (visit[nr][nc] == False) and graph[nr][nc] > n:
      dfs(nr, nc, n)
      
for n in range(2, level+1):
  visit = [[False] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if graph[i][j] > n and visit[i][j] == False:
        dfs(i, j, n)
        cnt += 1
  mx = max(mx, cnt)
  cnt = 0
  
print(mx)