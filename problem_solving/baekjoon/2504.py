#분배법칙
import sys
bracket = sys.stdin.readline()
result = 0
tmp = 1
stack = []

for i in range(len(bracket)):
  if bracket[i] == '(':
    stack.append(bracket[i])
    tmp *= 2
  elif bracket[i] == '[':
    stack.append(bracket[i])
    tmp *= 3
  elif bracket[i] == ')':
    if not stack or stack[-1] == '[':
      result = 0
      break
    if bracket[i-1] == '(': #stack[-1]이면 계속 더하게 됨
      result += tmp
    stack.pop()
    tmp //= 2
  elif bracket[i] == ']':
    if not stack or stack[-1] == '(':
      result = 0
      break
    if bracket[i-1] == '[':
      result += tmp
    stack.pop()
    tmp //= 3
    
print(result)