# Node
# Tree
# 값이 없으면 node를 추가 height = 1
# 값이 있으면 left 또는 right에 


class Node:
  def __init__(self, key, height, left=None, right=None):
    self.key = key
    self.height = height
    self.left = left
    self.right = right
    
class AVL:
  def __init__(self):
    self.root = None
    
  def get_height(self, n):
    if n == None:
      return 0
    return n.height
    
  def put(self, key):
    self.root = self.put_item(self.root, key)
  
  def put_item(self, n, key):
    if n == None:
      return Node(key, 1)
    if n.key > key:
      n.left = self.put_item(n.left, key)
    elif n.key < key:
      n.right = self.put_item(n.right, key)
    n.height = max(self.get_height(n.left), self.get_height(n.right)) + 1
    return self.balance(n)
  
  def balance(self, n):
    if self.bf(n) > 1:
      if self.bf(n.left) < 0:
        n.left = self.rotate_######################
    elif self.bf(n) < 1:
      if self.bf(n.right) > 0:
        n.right
        
    return n
    
  def bf(self, n):
    return self.get_height(n.left) - self.get_height(n.right)