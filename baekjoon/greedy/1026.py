import sys
N = int(sys.stdin.readline())
sum = 0
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2)
arr2.reverse()

for i in range(N):
    sum += arr1[i] * arr2[i]

print(sum)