class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        list = ["+","/","*","-"]
        stack = []
        
        for i in tokens:
            if i not in list:
                stack.append(i)
            else:
                if i == "+":
                    result = (int(stack[-2])) + (int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))
                elif i == "/":
                    if int(stack[-2]) < 0 and int(stack[-1]) > 0:
                        result = ceil(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                    elif  int(stack[-2]) > 0 and int(stack[-1]) < 0:
                        result = ceil(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                    else:
                        result = floor(int(stack[-2]) / int(stack[-1]))
                        stack.pop()
                        stack.pop()
                        stack.append(str(result))
                       
                elif i == "*":
                    result = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))
                else:
                    result = (int(stack[-2])) - (int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))
                               
        return stack[0]
                
