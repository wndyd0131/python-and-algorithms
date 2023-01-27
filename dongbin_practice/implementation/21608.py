import sys
N = int(sys.stdin.readline())
arr = list()
table = [[0 for _ in range(N)] for _ in range(N)]

dr = [-1, 1, 0, 0] # U, D
dc = [0, 0, -1, 1] # L, R

for i in range(N*N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for l in range(N*N): # 리스트
    tmp = []
    cur = arr[l][0]
    likeList = arr[l][1:]
    for i in range(N): # 테이블
        for j in range(N):
            if table[i][j] == 0:
                exist = 0
                empty = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if table[nr][nc] in likeList:
                            exist += 1
                        if table[nr][nc] == 0: # else로 했었지만, 값이 있는 상태로 포함되지 않을 수도 있기 때문에 0일 경우로 수정
                            empty += 1
                tmp.append([exist, empty, i, j])
    tmp.sort(key = lambda x: (-x[0], -x[1], x[2], x[3])) # list sort
    table[tmp[0][2]][tmp[0][3]] = cur
            
arr.sort()
result = 0
            
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if table[nr][nc] in arr[table[i][j]-1]:
                    cnt += 1
            if cnt != 0:
                result += 10 ** (cnt-1)

print(result)

#             3
# 4 2 5 1 7
# 3 1 9 4 5
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4