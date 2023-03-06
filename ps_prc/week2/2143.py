import sys
sys.setrecursionlimit(10 ** 6)

cnt = 0
Acounter = dict()
Bcounter = dict()

T = int(sys.stdin.readline())

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    for j in range(i, N):
        s = sum(arr1[i:j+1])
        if s in Acounter:
            Acounter[s] += 1
        else:
            Acounter[s] = 1

M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    for j in range(i, M):
        s = sum(arr2[i:j+1])
        if s in Bcounter:
            Bcounter[s] += 1
        else:
            Bcounter[s] = 1

for key in Acounter.keys():
    if (T - key) in Bcounter:
        cnt += Acounter[key] * Bcounter[T-key]


print(cnt)