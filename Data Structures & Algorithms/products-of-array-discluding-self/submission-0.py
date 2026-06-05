class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pre, post = [], []
        
        pre_temp = 1
        for i, num in enumerate(nums):
            if i == 0:
                pre.append(1)
                continue
            pre_temp *= nums[i - 1]
            pre.append(pre_temp)

        post_temp = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post.append(1)
                continue
            post_temp *= nums[i + 1]
            post.append(post_temp)
        print(post)
        post.reverse()
        
        return [pr*po for pr,po in zip(pre, post)]
            
