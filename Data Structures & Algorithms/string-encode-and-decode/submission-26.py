class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "".join(f"{len(s)}#{s}" for s in strs)
        print("encoded: ", res )
        return res



    def decode(self, s: str) -> List[str]:
        
        res = []

        l, r = 0, 0
        while l < len(s):
            while s[r] != "#":
                r+=1
            
            size = int(s[l:r])

            l = r + 1
            r += size + 1

            res.append(s[l:r])
    
            l = r

        return res


            
            
