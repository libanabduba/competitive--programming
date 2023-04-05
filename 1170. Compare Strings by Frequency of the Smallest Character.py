class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(string):
            dic = Counter(string)
            prevchar = float("inf")
            ans = 0
            for char,freq in dic.items():
                if ord(char) < prevchar:
                    ans = dic[char]
                    prevchar = ord(char)
            return ans

        
        search_list = []
        # print(f(words[0]))

        for word in words:
            search_list.append(f(word))

        search_list.sort()
        result = []
        n = len(search_list)
        for word in queries:
            left = 0
            right = len(search_list) - 1
            count = len(search_list)
            while left <= right:
                mid = left + (right -left)//2

                if f(word) < search_list[mid]:
                    count = min(count,mid)
                    right = mid - 1
                    # ans = min(ans, mid)
                else:
                    left = mid + 1


            result.append(n - count)
        return result
