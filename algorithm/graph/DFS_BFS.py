from collections import deque

def dfs(graph, v, visited):
  print(v, end = ' ')
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
    


def bfs(graph, v, visited):
  visited = [False] * (N + 1)
  q = deque()

  q.append(v)
  visited[v] = True
  
  while q:
    cur = q.popleft() #팝
    print(cur, end = ' ') #출력
    for i in graph[cur]: #그래프 접근
      if not visited[i]:
        q.append(i) #큐에 넣기
        visited[i] = True
        

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

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