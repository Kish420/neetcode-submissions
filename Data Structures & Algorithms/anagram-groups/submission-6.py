from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for i in strs:
            sorted_string = str(sorted(i))

            anaMap[sorted_string].append(i)

        return list(anaMap.values())
        