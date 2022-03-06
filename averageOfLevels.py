# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        arr = []
        
        while queue:
            size = len(queue)
            sum = 0
            for i in range(size):
                current = queue.popleft()
                sum += current.val
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)       
            arr.append(sum/size)
                
                
        return arr
