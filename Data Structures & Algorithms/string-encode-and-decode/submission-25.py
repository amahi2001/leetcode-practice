class Solution:

    def encode(self, strs: List[str]) -> str:
        #len#word
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        

        res = []

        l = 0
        while l < len(s):
            r = l

            # get number
            while s[r] != "#":
                r +=1

            length = int(s[l:r])

            # reposition the ptrs to get word
            l = r + 1
            r = l + length
            word = s[l:r]

            res.append(word)
            
            l = r

        return res



            