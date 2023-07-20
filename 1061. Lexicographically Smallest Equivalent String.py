class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = [i for i in range(26)]
        size = [1] * 26
        smallest =  [i for i in range(26)]

        def find(x):
          
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if smallest[root_x] < smallest[root_y]:
                smallest[root_y] = smallest[root_x]
            else:
                smallest[root_x] = smallest[root_y]

            if root_x != root_y:
                if size[root_x] < size[root_y]:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]
                else:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]

        for chars1, chars2 in zip(s1,s2):
            union(ord(chars1) - ord("a"), ord(chars2) - ord("a"))

        ans = ""


        for char in baseStr:
           root = find(ord(char) - ord("a"))
           ans += chr(smallest[root] + ord("a"))

        return ans



            






        

        

          
