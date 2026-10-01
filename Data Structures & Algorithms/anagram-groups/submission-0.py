class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        output = []

        for i in strs:
            string = str(sorted(i))
            if string in anaMap:
                anaMap[string].append(i)

            else:
                anaMap[string] = [i]

        for key in anaMap:
            output.append(anaMap[key])

        return output
        