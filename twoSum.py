class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        list = []
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp == target:
                list.append(left +1)
                list.append(right+ 1)
                break
            elif temp < target:
                left += 1
            else:
                right -= 1
                
        return list
                
            
        
        
