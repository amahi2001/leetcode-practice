class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        

        freq = [[] for x in range(len(nums) + 1)]

        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1


        for num, count in count.items():
            freq[count].append(num)

        res = []
        for sub in reversed(freq):
            for x in sub:
                res.append(x)
                if len(res) == k:
                    return res
            