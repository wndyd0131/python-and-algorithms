stack = []
flag = 0
while(True):
  line = input()
  if line == '.':
    break
  for i in range(len(line)):
    if line[i] == '(' or line[i] == '[':
      stack.append(line[i])
    elif line[i] == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        flag = 1
        break
    elif line[i] == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        flag = 1
        break
  if not stack and flag == 0:
    print("yes")
  else:
    print("no")
    stack = []
    flag = 0