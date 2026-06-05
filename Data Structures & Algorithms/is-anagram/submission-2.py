class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s_len:=len(s)) != len(t):
            return False

        t_count, s_count = {}, {}
        for i in range(s_len):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        return t_count == s_count