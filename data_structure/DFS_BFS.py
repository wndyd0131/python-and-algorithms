from collections import deque

def dfs(graph, v, visited):
  print(v, end = ' ')
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
    


def bfs(graph, v, visited):
  visited = [False] * (N + 1)
  needed = deque()

  needed.append(v)
  visited[v] = True
  
  while needed:
    node = needed.popleft()
    print(node, end = ' ')
    for i in graph[node]:
      if not visited[i]:
        needed.append(i)
        visited[i] = True
        

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1) #이 visted는 꼭 글로벌하게 되어야 하는가?

for i in range(M):
  num1, num2 = input().split()
  num1, num2 = int(num1), int(num2)
  graph[num1].append(num2)
  graph[num2].append(num1)
  graph[num1].sort()
  graph[num2].sort()

dfs(graph, V, visited)
print()
bfs(graph, V, visited)





#연습해본 코드

def d_f_s(graph, v, visited):
  print(v, end = ' ');
  visited[v] = True;
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited);

def b_f_s(graph, v, visited):
  visited = [False] * (N + 1)
  queue = deque()
  queue.append(graph[v])
  visited[v] = True
  
  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True