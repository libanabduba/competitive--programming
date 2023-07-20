class Solution:
    def __init__(self):
        self.parent = {}
        
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_to_name = {}
        
       
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                self.union(email, account[1])
                email_to_name[email] = name

    
        merged_accounts = {}
        for email in email_to_name:
            parent = self.find(email)
            if parent not in merged_accounts:
                merged_accounts[parent] = []
            merged_accounts[parent].append(email)
        
        result = []
        for parent, emails in merged_accounts.items():
            result.append([email_to_name[parent]] + sorted(emails))
        
        
        return result
