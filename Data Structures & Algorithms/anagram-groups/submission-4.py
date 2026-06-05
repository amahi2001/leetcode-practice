class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for s in strs:

            #arr of 26 where each idx reps letter 
            # e.g "abc" = [1, 1, 1, ....]
            # e.d "acd" = [1, 0, 1, 1, ...]
            word_key = [0] * 26 
            for c in s:
                letter_num = ord(c) - ord("a")
                word_key[letter_num] += 1

            res[tuple(word_key)].append(s)

        return list(res.values())

