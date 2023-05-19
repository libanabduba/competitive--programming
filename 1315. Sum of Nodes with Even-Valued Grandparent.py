# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def traverse(node, parent, grandparent):
            if not node:
                return 0

            # Check if the grandparent value is even
            grandparent_sum = node.val if grandparent and grandparent.val % 2 == 0 else 0

            # Traverse left and right subtrees
            left_sum = traverse(node.left, node, parent)
            right_sum = traverse(node.right, node, parent)

            return grandparent_sum + left_sum + right_sum

        return traverse(root, None, None)
