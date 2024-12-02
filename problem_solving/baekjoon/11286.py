import sys, heapq
heap = []
value = 0
N = int(sys.stdin.readline())
for i in range(N):
  input = int(sys.stdin.readline())
  if input == 0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    heapq.heappush(heap, (abs(input), input))
    

# heapq는 튜플도 가능하다
# 튜플 (abs(값), 값) 을 사용해서 절댓값이랑 비교하되 절댓값이 같은 값끼리는 원래 값과 비교하도록 할 수 있음