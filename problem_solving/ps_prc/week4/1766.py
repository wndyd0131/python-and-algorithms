import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
degree = [0] * (n+1)
queue = []
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(n):
    if degree[i+1] == 0: # degree가 0인거는 우선순위큐에다가 삽입
        heapq.heappush(queue, i+1)
        degree[i+1] = -1

while queue:
    for i in range(len(queue)):
        popped = heapq.heappop(queue)
        answer.append(popped)
        while(graph[popped]):
            degree[graph[popped].pop()] -= 1
        for i in range(n):
            if degree[i+1] == 0:
                heapq.heappush(queue, i+1)
                degree[i+1] = -1

for i in answer:
    print(i, end=' ')
print()
