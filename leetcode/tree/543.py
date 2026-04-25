# 543. Diameter of Binary Tree
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
        # Diameter = Longest path between any two nodes
        # Current node diameter = left height + right height
        # res = 0
        # 1. Use DFS to recursively search the tress
        # 2. If not node, return 0
        # 3. Else
        # leftHeight = diameterOfBinaryTree(left)
        # rightHeight = diameterOfBinaryTree(right)
        # res = max(leftHeight + rightHeight, res)
        # return max(leftHeight, rightHeight) + 1
    Time complexity: O(N)
    Space complexity: O(H)
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left_max_h = dfs(node.left)
            right_max_h = dfs(node.right)

            self.res = max(left_max_h + right_max_h, self.res)
            return max(left_max_h, right_max_h) + 1

        dfs(root)
        return self.res


