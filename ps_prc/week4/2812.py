import sys

def solution(nums, N, K):
  for i in range(len(nums)):
    num = int(nums[i])
    while stack:
      if num > stack[-1]:
        if len(stack)+len(nums[i:]) > N-K:
          stack.pop()
        else:
          stack.append(num)
          break
      else:
        if len(stack) == N-K:
          break
        else:
          stack.append(num)
          break
    if len(stack) == 0:
      stack.append(num)

stack = []
N, K = list(map(int, sys.stdin.readline().split()))
nums = sys.stdin.readline().rstrip()
solution(nums, N, K)

for i in range(len(stack)):
  print(stack[i], end="")