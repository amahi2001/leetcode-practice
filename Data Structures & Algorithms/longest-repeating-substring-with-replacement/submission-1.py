class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0

        count = {}        
        maxFreq = 0

        l = 0
        for r, c in enumerate(s):
            
            # update count of s[r]
            count[c] = count.get(c, 0) + 1

            # update letter with highest freq
            maxFreq = max(maxFreq, count[c])

            # window size = (r-l+1)
            #while window size minus most frequent char count IS GREATER than k
            # -> we CANT make k subs, so we have to move lftptr + update count
            while ((r-l+1) - maxFreq) > k:
                count[s[l]] -= 1
                l+=1

            longest = max(longest, r-l+1)
        
        return longest
