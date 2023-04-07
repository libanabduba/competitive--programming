# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        
        def helper(root):
            if not root:
                return 0, 0
            # if not root.left and not root.right:
            #     return root.val, 1

            sumLeft, sizeLeft = helper(root.left)
            sumRight, sizeRight= helper(root.right)

            avg = (sumLeft + sumRight + root.val)//(sizeLeft + sizeRight + 1)
            # print(avg, root.val)

            if avg == root.val:
                self.ans += 1

            return (sumLeft + sumRight + root.val) , (sizeLeft + sizeRight + 1)

        helper(root)

        return self.ans
