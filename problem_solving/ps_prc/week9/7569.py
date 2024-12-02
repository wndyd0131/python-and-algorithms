'''
토마토를 창고에 보관하는 격자모양의 상자들의 크기와
익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지,
그 최소 일수를 구하는 프로그램을 작성하라
'''

'''
저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

'''
더이상 0이 없으면 일수 출력
'''
import sys
from collections import deque
queue = deque([])
M, N, H = map(int, sys.stdin.readline().split())
direction = [[-1, 0, 0] , [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
h = -1
graph = [[[0 for col in range(M)] for row in range(N)] for depth in range(H)]
for i in range(N*H):
    if i % N == 0:
        h += 1
    graph[h][i%N] = list(map(int, sys.stdin.readline().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

def bfs():
    cnt = -1
    while(queue):
        cnt += 1
        for i in range(len(queue)):
            cur_idx = queue.popleft()
            h = cur_idx[0]
            r = cur_idx[1]
            c = cur_idx[2]

            for j in range(6):
                nh = h + direction[j][0]
                nc = c + direction[j][1]
                nr = r + direction[j][2]
                if nh >= 0 and nh < H and nc >= 0 and nc < M and nr >= 0 and nr < N:
                    if graph[nh][nr][nc] == 0:
                        queue.append((nh, nr, nc))
                        graph[nh][nr][nc] = 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    print(-1)
                    return
    print(cnt)

bfs()
