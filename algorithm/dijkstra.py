inf = float('inf')
node_num = 6

graph = [[0, 2, 5, 3, inf, inf],
     [2, 0, 7, inf, inf, 9],
     [5, 7, 0, 1, 2, 5],
     [3, inf, 1, 0, 7, inf],
     [inf, inf, 2, 7, 0, 2],
     [inf, 9, 5, inf, 2, 0]
     ]

d = []
v = [0 for _ in range(node_num)]

def get_smallest_index(arr):
    smallest = float('inf')
    index = 0
    for i in range(node_num):
        if not v[i] and arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

def dijkstra(start):
    for i in graph[start]: # choose source node
        d.append(i)
    v[start] = True # set source node as visited
    for i in range(node_num-1):
        cur_idx = get_smallest_index(d)
        v[cur_idx] = True
        for j in range(node_num):
            if not v[j]:
                if d[cur_idx] + graph[cur_idx][j] < d[j]:
                    d[j] = d[cur_idx] + graph[cur_idx][j]

dijkstra(0)
for i in d:
    print(i)

'''
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 짧은 노드 선택
4. 해당 노드의 이웃 노드로의 비용 계산
3-4 반복
'''