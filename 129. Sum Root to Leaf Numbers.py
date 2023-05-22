# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.total_sum = 0
        
        def dfs(node, path_sum):
            if not node:
                return
            
            # Update the path sum with the current node's value
            path_sum = path_sum * 10 + node.val
            
            # If the current node is a leaf node, update the total sum
            if not node.left and not node.right:
                self.total_sum += path_sum
            
            # Recursively traverse the left and right subtrees
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

        dfs(root, 0)
        return  self.total_sum


            




            
