import sys
count = 0
flag = 0

T = int(sys.stdin.readline())
for _ in range(T):
  arr = [0 for x in range(26)]
  text = sys.stdin.readline().strip()
  prev = text[0]
  for i in range(len(text)):
    if arr[ord(text[i])-97] == -1:
      flag = 1
      break
    if text[i] != prev:
      arr[ord(prev) - 97] = -1
    prev = text[i]
  if flag == 1:
    flag = 0
  else:
    count += 1
print(count)