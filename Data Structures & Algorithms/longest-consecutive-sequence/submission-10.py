class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)


        longest = 0
        for num in numset:
            
            probe = 0
            while (num - probe) in numset:
                probe+=1

                longest = max(longest, probe)
        
        return longest

