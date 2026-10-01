class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            char = [0] * 26
            for c in i:
                char[ord(c) - ord('a')] += 1

            res[tuple(char)].append(i)

        return list(res.values())
        