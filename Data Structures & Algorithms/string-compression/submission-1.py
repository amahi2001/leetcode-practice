class Solution:
    def compress(self, chars: List[str]) -> int:
        
        res = ""
        l = 0

        while l < len(chars):
            res+=chars[l]
            
            #set r ahead of l
            r = l + 1
            
            # while the next char is the same
            # -> inc r
            count = 1
            while r < len(chars) and chars[l] == chars[r]:
                r+=1
                count+=1
            
            #if the count is greater than 1 ->add count to res
            if count > 1:
                res+=str(count)
            
            # move l to r
            l = r
        
        for i, c in enumerate(res):
            chars[i] = c

        return len(res)        




