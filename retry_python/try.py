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
# lst[i]를 기준으로 sort
# N까지 반복하면서 lst[j]보다 크거나 같은 수가 있을 때마다 count를 올린다
# max값을 구한다
# 끝나는 시간이 가장 빠른 시간으로?

#11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8 
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14