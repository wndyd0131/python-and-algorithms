import sys
l = sys.stdin.readline().split()
for i in range(len(l)):
  l[i] = ','.join(l[i]).split(',')
  l[i].reverse()
  l[i] = int(''.join(l[i]))
print(max(l))