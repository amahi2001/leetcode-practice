class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pre, post = [1], [1]
        num_len = len(nums)

        temp = 1
        for i, n in enumerate(nums):
            if i == 0:
                continue    
            temp *= nums[i-1]
            pre.append(temp)
        
        temp = 1
        for i in range(num_len - 1, -1, -1):
            if i == num_len - 1: 
                continue
            temp *= nums[i + 1]
            post.append(temp)

        post.reverse()


        return [pr*po for pr, po in zip(pre,post)]
