class Node:
  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right
    
class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, key):
    self.root = self._insert_key(self.root, key)
    
  def _insert_key(self, node, key):
    if node == None:
      node = Node(key)
    else:
      if node.key >= key:
        node.left = self._insert_key(node.left, key)
      else:
        node.right = self._insert_key(node.right, key)
    return node
  
  def search(self, key):
    searched = self._search_key(self.root, key)
    return searched
  
  def _search_key(self, node, key):
    if node == None:
      return False
    elif node.key == key:
      return True
    else:
      if node.key > key:
        return self._search_key(node.left, key)
      else:
        return self._search_key(node.right, key)
      
  def delete(self, node, key):
    self.root, deleted = self._delete_key(self.root, key)
    return deleted
  
  def _delete_key(self, node, key):
    if node is None:
      return node, False
    
    deleted = False
    
    if node.key == key:
      deleted = True
      if node.left and node.right:
        parent, child = node, node.right
        while child.left is not None:
          parent, child = child, child.left
        child.left = node.left
        if parent != node:
          parent.left = child.right
          child.right = node.right
        node = child
      elif node.left or node.right:
        node = node.left or node.right
      else:
        node = None
    else:
      if node.key >= key:
        node.left, deleted = self._delete_key(node.left, key)
      else:
        node.right, deleted = self._delete_key(node.right, key)
    return node, deleted        
      
if __name__ == '__main__':
  tree = BST()
  tree.insert(4)
  tree.insert(1)
  tree.insert(8)
  tree.insert(9)
  tree.insert(5)
  
  ret = tree.search(0)
  print(ret)