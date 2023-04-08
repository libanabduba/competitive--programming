# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root,sum):
            if not root: return 0

            res = 0

            if root.val == sum:
               res += 1

            res += dfs(root.left, sum - root.val)
            res += dfs(root.right, sum - root.val)

            return res


        if not root: return 0

        return self.pathSum(root.left,targetSum) + dfs(root,targetSum) + self.pathSum(root.right,targetSum)
        
        



        
