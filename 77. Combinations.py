class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        nums = [num for num in range(1, n+ 1)]

        

        def backtrack(index, combination):

            if len(combination) == k:
                combinations.append(combination[:])
                return 

            if index >= n:
                return 

            
            combination.append(nums[index])

            backtrack(index+1, combination)

            combination.pop()

            backtrack(index+1, combination)

        backtrack(0,[])
        return combinations
