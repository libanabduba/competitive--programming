class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # ans = []

        # def helper(word):
        #     freq1 = Counter(word)
            
        #     flag = True

        #     for w in words2:
        #         freq2 = Counter(w)

        #         for letter in freq2:
        #             if letter not in freq1 or freq2[letter] > freq1[letter]:
        #                 flag = False
        #                 break

        #         if not flag: break
            
        #     if flag: ans.append(word)

               

        # for word in words1:
        #     helper(word)

        # return ans


        merged = [0] * 26

        for word in words2:

            freq = Counter(word)
            
            for char in freq:
                number_char = ord(char) - ord('a')
                merged[number_char] = max(merged[number_char], freq[char])
        print(merged)
        flag = True
        
        result = []
        for word in words1:
            freq = Counter(word)

           

            for val in range(len(merged)):
                
                if merged[val] != 0 and merged[val] > freq[chr(val + ord('a'))]:
                    flag = False
                    print(word, "hello")
                    break

            if flag: result.append(word)

            flag = True


        return result

        

        


              







        
