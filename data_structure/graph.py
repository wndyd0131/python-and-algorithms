class Graph():
  def __init__(self):
    self.graph = {}
    
  def addVertex(self, V):
    self.graph[V] = []
    
  def addEdge(self, start, end):
    self.graph[start].append(end)