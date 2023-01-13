import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst = sorted(lst)
result = 0
for i in range(1, N+1):
    for j in range(i):
        result += lst[j]

print(result)