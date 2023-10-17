class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        
    def charToIndex(self,char):
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:

        tempRoot = self.root

        for char in word:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                tempRoot.children[indx] = TrieNode()

            tempRoot = tempRoot.children[indx]


        tempRoot.isEnd = True


    
    def search(self, word: str) -> bool:
        tempRoot = self.root

        for char in word:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                return False

            tempRoot = tempRoot.children[indx]


        return tempRoot.isEnd
      

    def startsWith(self, prefix: str) -> bool:
        tempRoot = self.root

        for char in prefix:

            indx = self.charToIndex(char)

            if not tempRoot.children[indx]:
                return False

            tempRoot =  tempRoot.children[indx]


        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
