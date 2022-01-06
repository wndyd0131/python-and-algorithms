#https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
  
  def append(self, data):
    cur = self.head
    while cur.next != None:
      cur = cur.next
    cur.next = Node(data)
    
  def print_all(self):
    cur = self.head
    while cur.next != None:
      print(cur.data)
      cur = cur.next
      
  def get_node(self, index):
    count = 0
    node = self.head
    while count < index:
      node = node.next
      count += 1
    return node
  
  def insert(self, index, data):
    new_node = Node(data)
    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return
    node = self.get_node(index-1)
    node.next = new_node
    new_node.next = node.next
  
  def delete(self, index):
    if index == 0:
      self.head = self.head.next
      return
    node = self.get_node(index-1)
    node.next = node.next.next