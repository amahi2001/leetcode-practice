class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        
        
        
        for i, k in enumerate(nums):
            
            #if k is positive and nums is sorted -> next num is larger
            # which would make it impossible to get 0 -> hence return here
            if k > 0:
                break

            # if k == the previous
            if i > 0 and k == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = k + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else: 
                    res.append([k, nums[l], nums[r]])                    
                    l+=1
                    r-=1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l+=1


        return res