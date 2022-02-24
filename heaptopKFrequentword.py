class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = Counter(words)
        freq = [(-1*freq,word) for word,freq in dict.items()]
        heapify(freq)
        ans = []
        for i in range(k):
            poped = heappop(freq)
            if len(ans) == 0:
                ans.append(poped[1])
            else:
                
                if dict[poped[1]] == dict[ans[-1]] and poped[1] < ans[-1]:
                    ans.append(poped[1])
                    ans[-1],ans[-2] = ans[-2],ans[-1]
                else:
                    ans.append(poped[1])
                    
        return ans
