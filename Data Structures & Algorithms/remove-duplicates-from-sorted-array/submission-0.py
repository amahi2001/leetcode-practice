class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        l = r = 1 # since len(nums) alays 


        while r < len(nums):
            print(r)
            #if the curr is unique:
             # set the leftptr to unique value
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
            r+=1
        
        return l
