class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        res = nums[0]


        for i in range(len(nums)):

            curP = nums[i]
            res = max(res, curP)
            for j in range(i + 1, len(nums)):
                curP *= nums[j]
                res = max(res, curP)

        return res
            