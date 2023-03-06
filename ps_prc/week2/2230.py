import sys

result = list()
arr = list()
N, M = list(map(int, sys.stdin.readline().split())) # N == 5, M == 3
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort() # 1 2 3 4 5
high = 0

for i in range(N):
    for j in range(high, N):
        if arr[j] - arr[i] >= M:
            result.append(arr[j] - arr[i])
            high = j
            break

print(min(result))