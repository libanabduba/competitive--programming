# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([root])
        arr2 = []
        if root == None:
            return None
        while q:
            maxi = q[0].val
            for i in range(len(q)):
                current = q.popleft()
                if current.val > maxi:
                    maxi = current.val
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)
            arr2.append(maxi)
        
        return arr2
