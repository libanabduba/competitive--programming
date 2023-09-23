class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        index =  len(pref)
        count = 0

        for word in words:
            if word[ :index] == pref:
                count += 1

        return count
