# Need Review
import sys
import copy
from collections import deque

empty = []
virus = []
mx = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if MAP[i][j] == 0:
      empty.append([i,j])
    if MAP[i][j] == 2:
      virus.append([i,j])

def bfs(map):
  zero_cnt = 0
  global mx
  q = deque([])
  visited = [[False] * m for _ in range(n)]
  
  for v in virus: # parent node 큐에 집어넣음
    q.append(v)

  while q:
    r, c = q.popleft()
    
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if (0 <= nr < n and 0 <= nc < m) and visited[nr][nc] == False and map[nr][nc] == 0:
        q.append([nr, nc])
        map[nr][nc] = 2
        visited[nr][nc] = True
      else:
        continue
  
  for i in range(n):
    for j in range(m):
      if map[i][j] == 0:
        zero_cnt += 1
  
  mx = max(mx, zero_cnt)

for i in range(len(empty)):
  for j in range(len(empty)):
    for k in range(len(empty)):
      r1, c1 = empty[i]
      r2, c2 = empty[j]
      r3, c3 = empty[k]
      
      MAP[r1][c1] = 1
      MAP[r2][c2] = 1
      MAP[r3][c3] = 1
      TEMP_MAP = copy.deepcopy(MAP)
      
      bfs(TEMP_MAP)
      
      MAP[r1][c1] = 0
      MAP[r2][c2] = 0
      MAP[r3][c3] = 0
      

print(mx)

# 2차원 배열에서 어떻게 1 3개로 모든 경우의 수를 체크하지?