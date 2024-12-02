#곱하기 혹은 더하기
import sys
string = sys.stdin.readline().strip()
result = 0

result = int(string[0])
  

for i in range(1, len(string)):
  if int(string[i]) <= 1 or result <= 1:
    result += int(string[i])
  else:
    result *= int(string[i])
    
print(result)