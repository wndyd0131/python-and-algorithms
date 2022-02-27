import sys
tel = {'A':1,'B':1,'C':1,'D':2,'E':2,'F':2,'G':3,'H':3,'I':3,'J':4,'K':4,'L':4,'M':5,'N':5,'O':5,'P':6,'Q':6,'R':6,'S':6,'T':7,'U':7,'V':7,'W':8,'X':8,'Y':8,'Z':8}
init_time = 2
time = 0
alpha = sys.stdin.readline().strip()
for i in range(len(alpha)):
  time += init_time + tel[alpha[i]]
print(time)