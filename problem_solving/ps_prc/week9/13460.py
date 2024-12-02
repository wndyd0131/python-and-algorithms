'''
조건:
M x M
# . B R 0
- R가 0에들어가야 함
- 4방향으로 기울이기 (더 이상 움직이지 않을 때까지)
- B가 구멍에 빠지면 실패
    - R이 0에 들어가도 B가 0에 들어갈 수 있음
- R과 B는 같은 칸에 있을 수 없음

결론:
- 기울여서 B가 아닌 R이 0을 만나면 통과
'''

'''
알고리즘:
- 최단 경로이기 때문에 bfs 그래프 탐색
    - bfs로 하나씩 길을 밟다보면 0에 가장 먼저 닿는 경우가 발생할 것임
'''

'''
구현:

- bfs:
    R은 아래에 따라 상호작용:
    - 왼쪽으로 움직일 때는 왼쪽에 # 또는 B 또는 0
    - 오른쪽으로는 오른쪽에 # 또는 B 또는 0
    - 위로는 위쪽에 # 또는 B 또는 0
    - 아래로는 아래에 # 또는 B 또는 0
    B은 아래에 따라 상호작용:
    - 왼쪽으로 움직일 때는 왼쪽에 # 또는 R 또는 0
    - 오른쪽으로는 오른쪽에 # 또는 R 또는 0
    - 위로는 위쪽에 # 또는 R 또는 0
    - 아래로는 아래에 # 또는 R 또는 0

    - # 만나면 멈춤
    - 서로를 만나면 이동거리가 더 많은 구슬은 이전 칸으로 롤백
    - 0을 만나면 소멸하되 조건에 따름
    - 10을 넘으면 종료

구슬 위치가 0인가
구슬 다음이 #인가
    구슬 위치가 같은가
빨강이 앞에 있나 파랑이 앞에 있나
    - 판단을 위해 이동거리 카운트
10을 넘어갔는가
더 이상 갈 곳이 없는가
'''

import sys
from collections import deque
queue = deque([])
r, c = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    temp = sys.stdin.readline().strip()
    for j in range(c):
        graph[i][j] = temp[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r_visited = [[False for _ in range(10)] for _ in range(10)]
b_visited = [[False for _ in range(10)] for _ in range(10)]

def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            rmov = 0
            bmov = 0
            nrx, nry, nbx, nby = rx, ry, bx, by
            while graph[nrx+dx[i]][nry+dy[i]] != '#' and graph[nrx][nry] != 'O':
                nrx += dx[i]
                nry += dy[i]
                rmov += 1
            while graph[nbx+dx[i]][nby+dy[i]] != '#' and graph[nbx][nby] != 'O':
                nbx += dx[i]
                nby += dy[i]
                bmov += 1
            if graph[nbx][nby] == 'O': #파란공이 들어감
                continue
            if graph[nrx][nry] == 'O': #빨간공이 들어감
                print(depth)
                return
            if nrx == nbx and nry == nby:
                if rmov > bmov:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not r_visited[nrx][nry] or not b_visited[nbx][nby]:
                r_visited[nrx][nry] = True
                b_visited[nbx][nby] = True

                queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j
queue.append((rx, ry, bx, by, 1))
r_visited[rx][ry] = True
b_visited[bx][by] = True

bfs()