from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for i in strs:
            anaMap[str(sorted(i))].append(i)

        res = []
        for i in anaMap.values():
            res.append(i)

        return res

        


        