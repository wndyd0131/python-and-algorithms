import sys

N = int(sys.stdin.readline())
string = "moo"
i = 1
while len(string) < N:
  orig_string = string
  mid_string = "m" + "o"*(i+2)
  string = orig_string + mid_string + orig_string
  i += 1

print(string)

if N >= 4:
  if N <= len(orig_string):
    print(orig_string[N-1])
  elif N > len(orig_string) and N <= len(orig_string + mid_string):
    if N > len(orig_string)+1:
      print("o")
    else:
      print("m")
  else:
    N = N - len(orig_string+mid_string)
    print(orig_string[N-1])
else:
  if N == 0:
    print("m")
  else:
    print("o")