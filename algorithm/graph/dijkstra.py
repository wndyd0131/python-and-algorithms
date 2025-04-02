import heapq

inf = float('inf')
node_num = 6

graph = [[0, 2, 5, 3, inf, inf],
     [2, 0, 7, inf, inf, 9],
     [5, 7, 0, 1, 2, 5],
     [3, inf, 1, 0, 7, inf],
     [inf, inf, 2, 7, 0, 2],
     [inf, 9, 5, inf, 2, 0]
     ]

d = [float('inf') for _ in range(node_num)]
v = [0 for _ in range(node_num)]

# List
def get_smallest_index(arr):
    smallest = float('inf')
    index = 0
    for i in range(node_num):
        if not v[i] and arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

# Priority queue
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0 # table becomes [0, inf, inf, inf...]
    while q:
        dist, cur_idx = heapq.heappop(q) # O(logV) # extractMin
        if d[cur_idx] < dist: # if distance table has shorter path already, it means heappop returned visited vertex
            continue
        for j in range(node_num):
            # if current distance + distance to vertex j < current distance to vertex j
            if d[cur_idx] + graph[cur_idx][j] < d[j]:
                # then update current distance to j to shorter path
                d[j] = d[cur_idx] + graph[cur_idx][j]
                heapq.heappush(q, (d[j], j)) # O(logV) # decreaseKey


dijkstra(0)
for i in d:
    print(i)

'''
1. Select source node
2. Initialize distance table d[]
3. Select the shortest distance node from table d[] that's not visited
4. Perform relaxation for edges of the selected node
5. Repeat 3-4 
'''