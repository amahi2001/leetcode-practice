class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for k in range(len(nums)):
            
            #if k is positive and nums is sorted -> next num is larger
            # which would make it impossible to get 0 -> hence return here
            if nums[k] > 0:
                continue

            # if k == the previous
            if k > 0 and nums[k] == nums[k-1]:
                continue

            l, r = k + 1, len(nums) - 1

            while l < r:
                threeSum = nums[k] + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else: 
                    res.append([nums[k], nums[l], nums[r]])                    
                    l+=1
                    r-=1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l+=1


        return res