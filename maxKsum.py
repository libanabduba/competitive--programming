   nums.sort()
        leftindex = 0
        rightindex = len(nums) - 1
        count = 0
        
        while leftindex < rightindex:
            if nums[leftindex] + nums[rightindex] == k:
                count += 1
                leftindex += 1
                rightindex -= 1
            elif nums[leftindex] + nums[rightindex] < k:
                leftindex += 1
            else:
                rightindex -= 1
        return count
        
