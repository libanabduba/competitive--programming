class Solution:
    def hasPathSum(self,node,s):
        ans = 0
        if node == None:
            return False
        subSum = s - node.val
 
        # If we reach a leaf node and sum becomes 0, then
        # return True
        if(subSum == 0 and node.left == None and node.right == None):
            return True
 
        # Otherwise check both subtrees
        if node.left is not None:
            ans = ans or self.hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or self.hasPathSum(node.right, subSum)
 
        return ans
