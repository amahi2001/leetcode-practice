class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }


        for c in s:
            
            # if c is open
            if c not in closeToOpen:
                stack.append(c)
            
            # if c is closed
            else:
                # if the last item on stack is a bracket pair match -> pop
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                
                # else it means NOT valid parenthesis
                else:
                    return False
        

        return not bool(stack)