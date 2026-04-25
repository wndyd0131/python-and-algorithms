# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    [Components]
    1. Good node
        - should be at least greater or equal to root
    '''
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if node == None:
                return 0
            good_node = 0
            if node.val >= cur_max:
                cur_max = node.val
                good_node = 1

            return good_node + dfs(node.left, cur_max) + dfs(node.right, cur_max)
        return dfs(root, root.val)