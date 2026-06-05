class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = [[] for _ in range(len(nums) + 1)]


        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        
        for n, count in counts.items():
            freq[count].append(n)

        
        res = []
        for sub_list in reversed(freq):
            for x in sub_list:
                res.append(x)
                if len(res) == k:
                    return res