# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        if not p and not q:
            return True
        
        if (p and q) and (p.val == q.val):
            # recursively check the left and right substrees:

            same_left = self.isSameTree(p.left, q.left)
            same_right = self.isSameTree(p.right, q.right)

            return same_left and same_right
            
        else:
            return False