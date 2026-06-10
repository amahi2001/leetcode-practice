class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pre, post = [1], [0] * len(nums)

        temp = 1
        for i in range(1, len(nums)):
            prev = nums[i-1]
            temp*=prev
            pre.append(temp)

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[i] = 1
                continue
            temp*=nums[i + 1]
            post[i] = temp

        res = []
        for pr,po in zip(pre, post):
            res.append(pr*po)
        
        return res


            
