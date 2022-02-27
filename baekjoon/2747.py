import sys
def fibo(T):
    if T == 0:
      return 0
    elif T == 1 or T == 2:
      return 1
    return fibo(T - 1) + fibo(T - 2)

T = int(sys.stdin.readline().strip())
print(fibo(T))