class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dic = Counter(words)

        heap = []

        for word, freq in dic.items():
            heappush(heap, (-1 * freq, word))
        
        res= []
        
        for _ in range(k):
            res.append(heappop(heap)[1])

        return res
