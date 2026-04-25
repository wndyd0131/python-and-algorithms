# 572. Subtree of Another Tree
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
        1. Compare tree and subtree
            2. For each node compare source subtree and target subtree
                - recursively check if left subtree or right subtree contains subtree
                    - if not tree2:
                        return True
                    - if not tree1:
                        return False
                    - if tree1 and tree2 are same
                        - then return True
    Time complexity: O(N * M)
    Space complexity: O(H + SubH) = O(H)
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)