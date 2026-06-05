class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        comp_dict = {}
        for i, num in enumerate(nums):
            comp = target - num

            if comp in comp_dict:
                return [comp_dict[comp], i]
            comp_dict[num] = i
