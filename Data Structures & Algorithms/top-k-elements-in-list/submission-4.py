class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for _ in range(len(nums) + 1)]


        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, count in count.items():
            freq[count].append(n)

        res = []
        for sub_list in reversed(freq):
            for n in sub_list:
                res.append(n)
                if len(res) == k:
                    return res
