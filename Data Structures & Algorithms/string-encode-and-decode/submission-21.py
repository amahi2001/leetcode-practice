class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=(f'{len(s)}#{s}')
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #based on how we decoded i will start at lenth
        while i < len(s):
            '''note that in slicing i.e x[i:j], 
               slice will end on j - 1'''
            # let j start at i. aka a length val
            #move j to a # position
            j = i
            while s[j] != '#':
                j += 1
            #once j is a #pos we know the previous must be length val
            length = int(s[i:j])
            #move i past j to new substr
            i = j+1
            #move j to i + length, j will now be at the end of str
            j = i + length
            #append the str to res
            res.append(s[i:j])
            #set i to the char after end of str
            i = j
        return res