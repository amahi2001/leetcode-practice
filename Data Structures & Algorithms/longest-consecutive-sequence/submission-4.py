class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        longest = 1


        for num in nums:
            #check if the num is part of a seq

            if num + 1 in nums:
                continue
            
            probe = 1
            while num - probe in nums:
                probe +=1
                longest = max(longest, probe)
        return longest