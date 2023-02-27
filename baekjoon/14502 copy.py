# 벌어졌다고 가정한다 -> 0이 최대가 나오는 경우
# 브루트포스로 벽 3개를 세우는 경우를 모두 계산
# -> DFS로 2를 채움
# -> for문으로 0 count
  
import sys
import copy

pos2 = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  for j in range(m):
    if MAP[i][j] == 2:
      pos2.append([i,j])

TEMP_MAP = copy.deepcopy(MAP)
cnt = 0
mx = 0


def dfs(x, y):
  # 시작점 x,y
  global TEMP_MAP
  for i in range(4):
    TEMP_MAP[x][y] = 2
    nr, nc = x + dr[i], y + dc[i]
    if 0 <= nr < n and 0 <= nc < n:
      if TEMP_MAP[nr][nc] == 0:
        dfs(nr, nc)

def makeWall(cnt):
  global TEMP_MAP
  global mx
  zero_cnt = 0
  if cnt == 3:
    for p in pos2:
      dfs(p[0], p[1])
    for i in range(n):
      for j in range(m):
        if TEMP_MAP[i][j] == 0:
          zero_cnt += 1
    mx = max(mx, zero_cnt)
    TEMP_MAP = copy.deepcopy(MAP)
    return
  
  for i in range(n):
    for j in range(m):
      if TEMP_MAP[i][j] == 0:
        TEMP_MAP[i][j] = 1
        makeWall(cnt + 1)
        
makeWall(0)

print(mx)