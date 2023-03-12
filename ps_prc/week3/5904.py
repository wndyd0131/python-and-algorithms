import sys

def repeat(string, cnt):
  if len(string) >= N:
    # print(string)
    print(string[N-1])
    return
  n_string = string + "m" + "o" * (cnt + 2) + string
  repeat(n_string, cnt+1)

N = int(sys.stdin.readline())
repeat("moo", 1)