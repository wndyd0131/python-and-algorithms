import sys
N, M, K = sys.stdin.readline().split()
N, M, K = int(N), int(M), int(K)
arr = list(map(int, sys.stdin.readline().split()))
sum = 0
arr = sorted(arr)
arr.reverse()
first = arr[0]
second = arr[1]
for i in range(M):
    if i != 0 and i % K == 0:
        sum += second
        continue
    sum += first

print(sum)