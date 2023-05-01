# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    
        def buildGraph():
            if not preorder:
                return None
        
            root = TreeNode(preorder[0])
            stack = [root]
            
            for val in preorder[1:]:
                node = TreeNode(val)
                if val < stack[-1].val:
                    stack[-1].left = node
                else:
                    while stack and val > stack[-1].val:
                        last = stack.pop()
                    last.right = node
                stack.append(node)
            
            return root
            
        return buildGraph()

        # def buildGraph(preorder):
        #     if len(preorder) == 1:
        #         return TreeNode(preorder[0])
        #     if not preorder:
        #         return None

        #     mid = len(preorder)//2
        #     root = TreeNode(preorder[mid])
            
        #     root.left = buildGraph(preorder[:mid])
        #     root.right = buildGraph(preorder[mid + 1:])


        #     return root


        return buildGraph(preorder)

