# 1823. Find the Winner of the Circular Game
class Solution:
  '''
  iterate through the array and pop by selecting target
  '''
  
  def findTheWinner(self, n: int, k: int) -> int:
      arr = list(range(1, n + 1))
      target = 0
      while len(arr) > 1:
          target = target + k - 1
          target = target % len(arr)
          arr.pop(target)
      return arr[0]
    
from collections import deque

class Solution:
  '''
  Use array as circular queue
  Example:
  [1,2,3,4,5], k = 2
  [2,3,4,5] pop
  [2,3,4,5,1] append
  [3,4,5,1] pop
  [3,4,5,1] pop
  [4,5,1,3] append
  [5,1,3] pop
  ...
  '''
  def findTheWinner(self, n: int, k: int) -> int:
      q = deque(range(1, n+1))
      while len(q) > 1:
          for _ in range(k-1):
              q.append(q.popleft())
          q.popleft()
      return q[0]