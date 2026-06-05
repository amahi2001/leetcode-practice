class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
    
        
        l, r = 0, 0
        res = []
        while l < len(s):

            r = l # right ptr starts w left

            while s[r] != "#": # this will always give us the correct "#" in first pass if s
                r +=1
            
            word_length = int(s[l: r])
            l = r + 1
            r = l + word_length

            word = s[l:r]
            res.append(word)
            l = r

        return res


            

