# DFS
'''
def dfs(node):
    if not node:
        return <base case>

    left = dfs(node.left)
    right = dfs(node.right)

    return <combine left, right, and node>
'''

# node-order BFS
'''
from collections import deque
def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        # check visited
        # process node

        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
'''

# level-order BFS
'''
from collections import deque
def bfs(root):
    q = deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            # check visited
            # process node

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
'''
