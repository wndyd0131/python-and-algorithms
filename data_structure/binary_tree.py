class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None
  
  def preorder(self, node):
    if node is not None:
      print(node)
      self.preorder(node.left)
      self.preorder(node.right)
      
  def make_root(self, node, l_node, r_node):
    if self.root == None:
      self.root = node
    node.left = l_node
    node.right = r_node
