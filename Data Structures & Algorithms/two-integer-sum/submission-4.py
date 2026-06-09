class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp_dict = {} # number, index

        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in comp_dict:
                return [comp_dict[diff], i]

            comp_dict[n] = i
        