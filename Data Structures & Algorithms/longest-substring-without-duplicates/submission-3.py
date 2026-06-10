class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        window = set()

        l = 0
        for r in range(len(s)):

            # if repeated character, increment l + remove l from set
            while s[r] in window:
                window.remove(s[l])
                l+=1
            
            window.add(s[r])
            longest = max(longest, len(window))

        return longest

