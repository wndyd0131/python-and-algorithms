import sys

alias_list = []
num_list = []

N, M = map(int, sys.stdin.readline().split())
alias = [sys.stdin.readline().split() for _ in range(N)]
alias.sort(key=lambda x: int(x[1]))
print(alias)
data_list = []
ptr = 0
for i in range(N):
    alias, num = sys.stdin.readline().split()
    alias_list.append(alias)
    num_list.append(num)

for i in alias_list:
    print(alias_list)

for i in range(M):
    data = int(sys.stdin.readline())
    data_list.append(data)

