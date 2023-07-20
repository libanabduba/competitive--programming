class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par={i:i for i in range(1,n+1)}
        rank=[1]*(n+1)
        def find(res):
            ver=res
            while par[ver]!=ver:
                par[ver]=par[par[ver]]
                ver=par[ver]
            return ver    
                
     
        ans=[]
        def union(e1,e2):
            pe1=find(e1)
            pe2=find(e2)

            if pe1!=pe2:
                if rank[pe1]>rank[pe2]:
                    par[pe2]=pe1
                    rank[pe1]+=rank[pe2]
                else:
                    par[pe1]=pe2
                    rank[pe1]+=rank[pe2] 
                return False    
            else:           
                return True
            
        for e1,e2 in edges:
            if union(e1,e2):
                return [e1,e2]
