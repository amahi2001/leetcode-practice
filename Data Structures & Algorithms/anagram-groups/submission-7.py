class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def str_to_sig(string: str) -> int:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] +=1
            return tuple(count)


        
        res = defaultdict(list)

        for s in strs:
            sig = str_to_sig(s)
            res[sig].append(s)

        return list(res.values())