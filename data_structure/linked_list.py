class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = Node()
    
  def append(self, data):
    cur = self.head
    while cur.next != None:
      cur = cur.next
    cur.next = Node(data)
  
  def get_node(self, index):
    i = 0
    cur = self.head
    while i < index:
      cur = cur.next
      i += 1
    return cur
  
  def insert(self, index, data):
    new_node = Node(data)
    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return
    node = self.get_node(index-1)
    temp = node.next
    node.next = new_node
    node.next.next = temp
  
  def delete(self, index):
    if index == 0:
      self.head = self.head.next
      return
    node = self.get_node(index-1)
    node.next = node.next.next
      
  def print(self):
    cur = self.head.next
    while cur != None:
      print(cur.data)
      cur = cur.next
      
if __name__ == '__main__':
  a = linked_list()
  a.append(4)
  a.append(5)
  a.delete(2)
  a.insert(1, 5)
  a.print()