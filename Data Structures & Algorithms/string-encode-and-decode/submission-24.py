class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:

        left = 0
        res = []
        while left < len(s):
            right = left
            
            # move left until symbol
            while s[right] != "#":
                right +=1
            
            # get the length
            length = int(s[left:right])
            
            #move left to start of word (right + 1)
            left = right + 1

            #move right to end of word
            right = left + length

            # get the word from s
            word = s[left:right]
            res.append(word)

            #move left to end of word
            left = right
        return res
