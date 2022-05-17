class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestion = []
        
    def add_suggestion(self,word):
        if len(self.suggestion) < 3:
            self.suggestion.append(word)

        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_suggestion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result
