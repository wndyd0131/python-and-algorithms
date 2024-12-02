from collections import deque

node_num = 7

d = [[] for _ in range(node_num+1)]
in_degree = [0 for _ in range(node_num+1)]

def topological_sort():
     q = deque()
     result = []
     for i in range(1, node_num+1):
          if in_degree[i] == 0:
               q.append(i)
     while q:
          cur = q.popleft()
          result.append(cur)
          for i in range(len(d[cur])):
               in_degree[d[cur][i]] -= 1
               if in_degree[d[cur][i]] == 0:
                    q.append(d[cur][i])
     return


d[1].append(2)
in_degree[2] += 1
d[1].append(5)
in_degree[5] += 1
d[2].append(3)
in_degree[3] += 1
d[3].append(4)
in_degree[4] += 1
d[4].append(6)
in_degree[6] += 1
d[5].append(6)
in_degree[6] += 1
d[6].append(7)
in_degree[7] += 1
topological_sort()