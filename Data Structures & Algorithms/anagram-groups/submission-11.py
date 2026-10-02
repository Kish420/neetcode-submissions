class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            char = [0] * 26
            for c in i:
                char[ord(c)-ord('a')] += 1
            output[tuple(char)].append(i)

        return list(output.values())
