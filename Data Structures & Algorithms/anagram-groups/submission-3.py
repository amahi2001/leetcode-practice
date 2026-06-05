class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for s in strs:

            word_key = [0] * 26

            for c in s:
                letter_num = ord(c) - ord("a")
                word_key[letter_num] += 1

            res[tuple(word_key)].append(s)

        return list(res.values())

