import sys
sys.setrecursionlimit(10 ** 6)
string = "moo"
N = int(sys.stdin.readline())

def bt(n, depth, b_len):
  new_length = 2*b_len + depth + 3
  
  if n < 4:
    return

  if new_length < n:
    bt(n, depth+1, new_length)
  else:
    if n > b_len and n <= b_len + depth + 3:
      if n - b_len == 1:
        print("m")
      else:
        print("o")
      return
    else:
      bt(n-(b_len+depth+3),1,3)

bt(N,1,3)