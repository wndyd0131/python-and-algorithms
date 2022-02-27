import sys
def factorial(T):
  if T == 0 or T == 1:
    return 1
  return T * factorial(T-1)
  
T = int(sys.stdin.readline().strip())
print(factorial(T))