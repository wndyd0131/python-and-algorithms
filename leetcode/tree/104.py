# 104. Maximum Depth of Binary Tree
'''
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
'''
from collections import deque
class Solution:
    '''
    Algorithms: BFS
    Steps:
        1. Init by putting root inside queue
        2. while queue
            for _ in range(queue)
                pop
                push left and push right
            record the depth
        3. return depth
    Time complexity: O(N)
    Space complexity: O(N)
    '''

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxDepth = 0
        if root != None:
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                maxDepth += 1
        return maxDepth

class Solution:
    '''
    Algorithms: BFS
    Steps:
        1. If node doesn't exist, return 0
        2. Recursively return max(left maxDepth, right maxDepth) + 1
    Time complexity: O(N)
    Space complexity: O(H)
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1