class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        longest = 1

        num_set = set(nums)
        for num in num_set:
            #check if the num is part of a seq

            if num + 1 in num_set:
                continue
            
            probe = 1
            while num - probe in num_set:
                probe +=1
                longest = max(longest, probe)
        return longest