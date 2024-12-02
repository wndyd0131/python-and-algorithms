import sys
def dfs(s):
    global cnt
    for nr in (s+graph[s], s-graph[s]):
        if 0 <= nr < N and v[nr] == 0:
            cnt+=1
            v[nr] = 1
            dfs(nr)
            


N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())
cnt = 1
v=[0]*N
dfs(S-1)

print(cnt)