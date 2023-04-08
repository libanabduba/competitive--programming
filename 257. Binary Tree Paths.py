# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        arr = []
        temp = []
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    temp.append(root.val)
                    temp2 = "->".join(list(map(str,temp)))
                    arr.append(temp2)
                    temp.pop()
                    return 

               
                temp.append(root.val)

                dfs(root.left)
                dfs(root.right)

                temp.pop()

                return

        dfs(root)
        return arr
            
