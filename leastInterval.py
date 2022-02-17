class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        freq = [i for i in dic.values()]
        max_fre = max(freq) 
        count = freq.count(max_fre)
       
                
        return max(len(tasks),(max_fre - 1) * (n + 1) + count)
            
