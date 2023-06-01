class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.dead = set()
        self.throne = defaultdict(list)
        

    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        self.order = []
        
        self.dfs(self.kingName)

        return self.order

    
    def dfs(self, node):
        if node not in self.dead:
            self.order.append(node)
        for child in self.throne[node]:
            self.dfs(child)





        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
