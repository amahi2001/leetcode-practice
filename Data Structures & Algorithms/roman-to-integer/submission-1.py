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


        res = 0
        for i, c in enumerate(s):

            # if the next val is increasing order -> subtract
            
            if (i + 1 < len(s)) and sym[c] < sym[s[i+1]]:
                res -= sym[c]
            else:
                res += sym[c]
        

        return res


            #else -> add