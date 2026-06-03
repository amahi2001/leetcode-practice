# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True

            if (p and q) and (p.val == q.val):
                left_same = isSameTree(p.left, q.left)
                right_same = isSameTree(p.right, q.right)
                return left_same and right_same
            
            return False


        if not root and not subRoot:
            return True

        q = deque([root])

        while q:
            n = q.popleft()
            if not n: continue

            if n.val == subRoot.val:
                if isSameTree(n, subRoot):
                    return True
            
            q.append(n.left)
            q.append(n.right)

        return False