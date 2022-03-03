class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        for employee in employees:
            if employee.id == id:
                parent = employee
                break
                
        print(parent)        
        def traversal(employees,parent,sum):
            if parent == None:
                return sum
            
            sum += parent.importance
            
            for i in parent.subordinates:
                for e in employees:
                    if e.id == i:
                        sum = traversal(employees,e,sum)
                        break
            return sum
        
        ans = traversal(employees,parent,0)
        return ans
