import sys
num = int(sys.stdin.readline().strip())
arr = [['' for x in range(num)] for _ in range(num)]
count = 1
biggest = 1

for i in range(num):
  st = sys.stdin.readline().strip()
  for j in range(num):
    arr[i][j] = st[j]

for i in range(num):
  if biggest == num:
    break
  
  for j in range(num):
    if j < num-1:
      arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
      for k in range(num): #가로 긴거
        count = 1
        for l in range(num-1):
          if arr[k][l] == arr[k][l+1]:
            count += 1            
          else:
            count = 1
          if count > biggest:
            biggest = count
      for k in range(num): #세로 긴거
        count = 1
        for l in range(num-1):
          if arr[l][k] == arr[l+1][k]:
            count += 1            
          else:
            count = 1
          if count > biggest:
            biggest = count
      arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        
    if i < num-1:
      arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
      for k in range(num): #가로 긴거
        count = 1
        for l in range(num-1):
          if arr[k][l] == arr[k][l+1]:
            count += 1            
          else:
            count = 1
          if count > biggest:
            biggest = count
      for k in range(num): #세로 긴거
        count = 1
        for l in range(num-1):
          if arr[l][k] == arr[l+1][k]:
            count += 1            
          else:
            count = 1
          if count > biggest:
            biggest = count
      arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]
  
print(biggest)

# 배운 것:
# 1) if else의 순서를 잘 구성하자
# 2) 배열의 범위를 무작정 한정 짓는 것보다 if문으로 무시하게 하는 방법도 있다
    # Mistake: 무작정 num-1까지만 돌게 하다가 [num-1][num-1]은 비교를 못하게 돼서 예외적으로 돌게 했는데도 안 됨
    # Solved: i와 j를 num-1이 아닌 num까지 다 돌게 하되, num-1일 때 각각 멈추게 해서 j가 num-1이여도 i는 계속 돌 수 있게 함
