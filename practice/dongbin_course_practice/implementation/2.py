#Bruteforce
# 24 * 60 * 60 = 86400 이기 때문에 컴퓨터가 충분히 브루트포싱할 수 있음
# 1초에 2000만번
import sys
h = int(sys.stdin.readline().strip())
cnt = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        cnt += 1

print(cnt)