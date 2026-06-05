class Solution:
    def romanToInt(self, s: str) -> int:
    
        sym = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # if it's single digit, return it
        if len(s) == 1:
            return sym[s[0]]

        l = 0
        res = 0
        for r in range(1, len(s)):
            lv, rv = sym[s[l]], sym[s[r]]
            if lv < rv: 
                res -= lv
            else: 
                res += lv
            
            l+=1
        
        res += sym[s[-1]]
        return res
