class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pre, post = [], []

        temp = 1
        for i, num in enumerate(nums):
            if i == 0:
                pre.append(temp)
                continue            
            temp*=nums[i-1]
            pre.append(temp)

        temp = 1
        reverse_nums = list(reversed(nums))
        for i, num in enumerate(reverse_nums):
            print(num)
            if i == 0:
                post.append(temp)
                continue            
            temp*=reverse_nums[i-1]
            post.append(temp)

        post.reverse()

        return [pr*po for pr,po in zip(pre, post)] 

        # [1,2,4,6]

        # 6, 4, 2, 1

            
            
            
            
        
        
