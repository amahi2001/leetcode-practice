# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node: TreeNode | None, left_bound: int, right_bound: int):
            '''Left and right are boundaries'''
            if not node:
                return True
            
            # if it doesn't meet the basic req's for binary tree -> False
            if not (left_bound < node.val < right_bound):
                return False

            # recursievley check left side
            # node.left/right becomes new node. to be valid BST:
            # 1. leftbbound < node.left < node.val => else not valid
            # 2. node.val < node.right < rightbound => else not valid
            left_valid = valid(node.left, left_bound, node.val)
            right_valid = valid(node.right, node.val, right_bound)

            return left_valid and right_valid

        # we set inital bounds to (inf, -inf)
        return valid(root, -math.inf, math.inf)
            
            