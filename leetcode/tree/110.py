# 110. Balanced Binary Tree
'''
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
'''

class Solution:
    '''
    Algorithms: DFS
    Steps:
        # 1. Define base case
            # if not node, return 0
        # 2. Recursion
            # left_h = dfs(node.left)
            # right_h = dfs(node.right)
            # if left height and right height difference > 1, then the tree is not balanced
            # return max_height + 1 := max(left_h, right_h) + 1
    Time complexity: O(N)
    Space complexity: O(H)
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            if abs(left_h - right_h) > 1:
                self.res = False
            return max(left_h, right_h) + 1
        dfs(root)
        return self.res