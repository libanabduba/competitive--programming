class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
    

        # def helper(index, prevIndex, memo):

        #     if index >= len(nums) : return 0

        #     if (index, prevIndex) in memo: return memo[(index, prevIndex)]

        #     l = 0 + helper(index + 1, prevIndex,memo)

        #     r = 0
        #     if prevIndex == float("-inf") or nums[index] > nums[prevIndex]:
        #         r = 1 + helper(index + 1, index,memo)

        #     memo[(index,prevIndex)] = max(l,r)

        #     return memo[(index,prevIndex)]


        # return helper(0, float('-inf'), {})

        def helper(target, arr):

            l, r = 0, len(arr) - 1

            index = float('inf')

            while l <= r:

                mid = (l + r)//2

                if arr[mid] > target:
                    index = min(mid, index)
                    r = mid - 1

                elif arr[mid] < target:
                    l = mid + 1

                else:
                    index = min(mid, index)
                    r = mid - 1

            return index




                    



        arr = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > arr[-1]:
                arr.append(nums[i])

            else:
                index = helper(nums[i], arr)

                arr[index] = nums[i]



        return len(arr)
