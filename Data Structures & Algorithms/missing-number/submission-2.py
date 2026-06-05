class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sum of array without missing using range(0...len(nums))
        true_sum = sum(range(len(nums) + 1))
        
        # sum of nums
        missing_sum = sum(nums)
        
        # return the difference
        return true_sum - missing_sum