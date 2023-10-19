class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.value = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.hashmap = {}
        
        
    def charToIndex(self,char):
        return ord(char) - ord("a")

    def insert(self, word: str, key: int) -> None:
        change = key - self.hashmap.get(word, 0)

        self.hashmap[word] = key

        tempRoot = self.root

        for char in word:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                tempRoot.children[indx] = TrieNode()

            tempRoot = tempRoot.children[indx]
            tempRoot.value += change


    def startsWith(self, prefix: str) -> int:
        tempRoot = self.root

        for char in prefix:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                return 0

            tempRoot =  tempRoot.children[indx]


        return tempRoot.value

class MapSum:

    def __init__(self):
       self.map = Trie()
        
    def insert(self, key: str, val: int) -> None:
        self.map.insert(key,val)
        
        
        

    def sum(self, prefix: str) -> int:
        
        return self.map.startsWith(prefix)

       





        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
