class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0


        l = 0
        while l < len(s):
            r = l + 1

            seen = {s[l]}

            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r+=1
            
            longest = max(longest, r-l)
            l += 1


        return longest
