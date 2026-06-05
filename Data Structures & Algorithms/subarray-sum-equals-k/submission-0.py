class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        
        cumsum = 0 #-> cum sum @idx i

        pre = {0:1} # cumsum : freq

        for num in nums:
            
            cumsum += num
            # At this point:
            # cumsum = sum of nums[0..i] (prefix sum up to current index)

            # We want subarrays that sum to k.
            # A subarray (j+1 .. i) sums to k if:
            #   cumsum(i) - cumsum(j) = k
            # Rearranged:
            #   cumsum(j) = cumsum(i) - k

            # So:
            # diff = the prefix sum we need to have seen before
            diff = cumsum - k

            # If we've seen this 'diff' before, each occurrence represents
            # a valid subarray ending at the current index
            if diff in pre:
                res += pre[diff]

            # Record current prefix sum for future subarrays
            # (so future indices can use this as their "starting point")
            pre[cumsum] = pre.get(cumsum, 0) + 1
        
        return res