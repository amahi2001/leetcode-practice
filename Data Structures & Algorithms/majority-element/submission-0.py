class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #boyer moore



        count = 0
        cand: int | None = None

        for n in nums:
            
            # if the count is 0, set new candidate (or first iteration)
            if count == 0:
                cand = n
        
            # if the curr is cand -> increment
            if n == cand:
                count +=1
            # else decrement
            else:
                count -=1
        
        return cand

        
        
        