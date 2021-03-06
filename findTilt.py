# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        def findsum(root):
            if root == None: return 0
            l = findsum(root.left)
            r = findsum(root.right)
            
            self.tilt += abs(l-r)
            return l + r + root.val
        
        findsum(root)
        return self.tilt
