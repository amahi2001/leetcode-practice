class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        #num (diff) : idx
        diff_dict = {}


        for i, num in enumerate(nums):

            diff = target - num


            if diff not in diff_dict:
                diff_dict[num] = i
            
            else:
                return [diff_dict[diff], i]