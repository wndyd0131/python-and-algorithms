# 비용: 키 가장 큰 - 키 가장 작은
# 답: 조별 비용의 합이 가장 작은 경우

import sys
lst = list()
sum = 0
N, K = sys.stdin.readline().split()
N, K = int(N), int(K)
members = list(map(int, sys.stdin.readline().split()))
for i in range(len(members)-1):
    lst.append(members[i+1]-members[i])
lst = sorted(lst, reverse=True)
for i in lst[(K-1):]:
    sum += i

print(sum)