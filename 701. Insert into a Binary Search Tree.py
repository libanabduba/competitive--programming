# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        current = root
        parent = root
        if root == None:
            return TreeNode(val)
        def insert(root,parent):
            
            if root:
                if root.val > val:
                    parent = root
                    insert(root.left,parent)
                else:
                    parent = root
                    insert(root.right,parent)
            else:
                node = TreeNode(val)
                if parent.val > val:
                    parent.left = node
                else:
                    parent.right = node

        
        insert(root,parent)

        return current
