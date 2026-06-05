class Solution:

    def get_str_key(self, s:str) -> tuple(int):
        count = [0] * 26
        for c in s:
            x = ord(c) - ord("a")
            count[x] += 1
        return tuple(count)
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        

        res = defaultdict(list) #key : list[words]


        for s in strs:

            str_key = self.get_str_key(s)

            res[str_key].append(s)

        
        return list(res.values())