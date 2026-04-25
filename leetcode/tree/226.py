# 226. Invert Binary Tree
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
class Solution:
    '''
    Algorithms: DFS
        Step:
            1. Recursively enter next node using DFS
            2. If node exists
                - then swap left and right
                - else return node
            3. return swapped node
    Time complexity: O(N)
    Space complexity: O(Height of Tree)
        - Balanced = O(logN)
        - Skewed = O(N)
    '''
    def dfs_invert(self, node):
        if not node:
            return node
        node.left, node.right = node.right, node.left
        node.left = self.dfs_invert(node.left)
        node.right = self.dfs_invert(node.right)
        return node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.dfs_invert(root)
        return res

class Solution:
    '''
    Same but independent version
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root