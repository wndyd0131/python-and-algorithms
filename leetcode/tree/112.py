# 112. Path Sum
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
    Algorithms: Preorder DFS
    1. Base case: if not root, return false
    2. Recursion
        1. curSum = targetSum - node
	        DFS (node, curSum)
        2. If leaf node and curSum == 0
            - then, return True
        3. Recurse with left node and right node
    Time complexity: O(N)
    Space complexity: O(H)
    '''
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        curSum = targetSum - root.val
        if not root.left and not root.right and curSum == 0:
            return True
        return self.hasPathSum(root.left, curSum) or self.hasPathSum(root.right, curSum)