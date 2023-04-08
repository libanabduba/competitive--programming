class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        result = []
        subset = []

        def dfs(index):
            if index >= len(nums):
               result.append(subset[::])
               return

            subset.append(nums[index])

            dfs(index + 1)

            subset.pop()

            dfs(index + 1)

            return 

        dfs(0)

        return result
            
