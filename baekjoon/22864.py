import sys
fatigue = 0
comp = 0
cmd = list(map(int, sys.stdin.readline().split()))
A,B,C,M = cmd[0], cmd[1], cmd[2], cmd[3]
for i in range(1, 25):
  if (fatigue + A) > M:
    fatigue -= C
    if fatigue < 0:
      fatigue = 0
  else:
    fatigue += A
    comp += B
print(comp)

# Bruteforce
# 24시간 일처리
# A=피로도 증가량, B=일 처리량, C=피로도 감소량, M=피로도 한계