
 class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        index = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
           
        while index < len(flowerbed):
            if flowerbed[index] == 1:
                index += 2
            else:
                if index == 0:
                    if flowerbed[index + 1] == 0:
                        n -= 1
                        if n == 0:
                            return True
                        index += 2
                        continue
                    else:
                        index += 1
                        continue
                
                if index == len(flowerbed) - 1:
                    if flowerbed[index - 1] == 0:
                        n -= 1
                        if n == 0:
                            return True
                        index += 2
                        continue
                if index > 0 and index < len(flowerbed) - 1:   
                    if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                        n -= 1
                        if n == 0:
                            return True
                        index += 2
                    else:
                        index += 1
                       
                    
        if n == 0:
            return True
        return False
            
