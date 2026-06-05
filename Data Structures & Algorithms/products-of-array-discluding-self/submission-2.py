class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pre, post = [1], [1]

        temp = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            
            temp*=nums[i-1]
            pre.append(temp)

        temp = 1
        for i in range((last:=len(nums)-1), -1, -1):
            if i == last:
                continue
            temp*=nums[i+1]
            post.append(temp)
        post.reverse()
        

        return [pr*po for pr,po in zip(pre, post)]
            



        # 6, 4, 2, 1

            
            
            
            
        
        
