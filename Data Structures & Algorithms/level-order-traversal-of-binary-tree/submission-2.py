# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        out = []
        q = deque([root])

        while q:
            # snapshot length before modifying q
            # this is the width of the current level
            q_len = len(q)
            level = []

            # for each item in the q_len -> pop the items and queue the sub items 
            for _ in range(q_len):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
                    level.append(n.val)

            if level:
                out.append(level)
        return out




        