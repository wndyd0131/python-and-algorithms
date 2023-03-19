import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

def solution(arr):
  for i in range(len(arr)):
    while stack:
      if arr[i] > stack[-1][0]:
        stack.pop()
      else:
        answer.append(stack[-1][1]+1)
        stack.append([arr[i],i])
        break
    if len(stack) == 0:
      answer.append(0)
      stack.append([arr[i],i])

solution(arr)
for i in range(len(answer)):
    print(answer[i], end = " ")
print()