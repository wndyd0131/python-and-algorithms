# 100. Same Tree
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
        Condition to consider:
            # p and q are same when both are None
            # p and q are same when both have same value
        Time complexity: O(N)
        Space complexity: O(H)
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.res = True
        def dfs(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    self.res = False
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
            else:
                if (node1 and not node2) or (not node1 and node2):
                    self.res = False
            return
        dfs(p, q)
        return self.res