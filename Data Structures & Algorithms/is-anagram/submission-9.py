class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)



        for l, count in s_count.items():
            
            if count != t_count[l]:
                return False
        return True