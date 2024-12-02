import sys
N = int(sys.stdin.readline())
count = 1
lst = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    temp[0], temp[1] = temp[1], temp[0]
    lst.append(temp)
lst = sorted(lst)
endTime = lst[0][0]
for i in range(1, N):
    if(lst[i][1] >= endTime):
        count += 1
        endTime = lst[i][0]
print(count)