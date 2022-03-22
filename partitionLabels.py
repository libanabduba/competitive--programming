class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        
        for i,value in enumerate(s):
            dic[value].append(i)
        
        # print(dic)
        
        left = 0
        right = dic[s[0]][-1]
        temp = left + 1
        arr = []
        
        while right < len(s):
            
            while temp < right:
                if dic[s[temp]][-1] > right:
                    right =  dic[s[temp]][-1]
                    
                temp += 1
                  
            arr.append(len(s[left:right+1]))
            # print(arr) 
            left = right + 1
            if left >= len(s):
                break
        
            temp = left + 1
            right = dic[s[left]][-1]
      
        return(arr)
           
