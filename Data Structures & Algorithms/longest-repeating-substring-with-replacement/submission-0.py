class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        l = 0
        longest = 0

        for r, c in enumerate(s):
            
            #count current char
            count[c] = count.get(c, 0) + 1

            #if windowSize - mostFreq <= k : then we can make k substitutins to make a repeating string
            #e.g if s=ABB & k=2 -> {A:1:, B:2} -> we can make <= 2 subs and have BBB
            if (r-l+1) - max(count.values()) <= k:
                #update longest
                longest = max(longest, r-l+1)
            #if it wonk't make a repeating string -> shift l up
            else:
                count[s[l]] -=1
                l+=1
        
        return longest
