class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # idx = count | vals is list of vals w/ that count
        freq = [[] for _ in range(len(nums) + 1)] #len of nums can be the highest freq

        counts = {} # num : count

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for n, count in counts.items():
            freq[count].append(n)

        res = []
        for sub_list in reversed(freq):
            for x in sub_list:
                res.append(x)
                if (len(res) == k):
                    return res




