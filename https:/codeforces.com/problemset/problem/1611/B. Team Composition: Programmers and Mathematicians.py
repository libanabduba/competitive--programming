
import math
def myfunc(a,b):
                    def helper(group):
                                        if a >= group and b >= group and (a + b) >= group * 4:
                                                            return True
                                        return False
                                        
                    low = 0
                    high = math.ceil((a+b)/4)
                    res = 0
                    
                    while low <= high:
                                        group = (low + high)//2
                                        
                                        if helper(group):
                                                            res = max(res,group)
                                                            low = group + 1
                                        else:
                                                            high = group - 1
                    return res
                                                            
                                        
                                                            
                    
                    
   
    

# Main code
t = int(input())

for i in range(t):
    a, b= list(map(int, input().split()))
    print(myfunc(a, b))
