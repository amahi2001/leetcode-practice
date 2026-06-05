class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        maxS = nums[0]

        cursum = 0


        for n in nums:

            #if cursum is neg => reset
            if cursum < 0:
                cursum = 0
            cursum += n

            maxS = max(maxS, cursum)

        return maxS
                