class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #count S
        s_count, t_count = {}, {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1


        for c, v in s_count.items():

            if t_count.get(c) != v:
                return False
        return True
