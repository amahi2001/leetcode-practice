class Solution:
    def isValid(self, s: str) -> bool:\

        if not s: 
            return True
        
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for x in s:
            
            if not stack and x in close_to_open:
                return False

            if x not in close_to_open:
                stack.append(x)
            
            elif stack and x in close_to_open:
                brack = stack.pop()

                if close_to_open[x] != brack:
                    return False

        return not bool(stack)