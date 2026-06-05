class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        

        true_sum = sum(range(len(nums) + 1))

        missing_sum = sum(nums)

        return true_sum - missing_sum