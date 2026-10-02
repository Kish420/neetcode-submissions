class Solution:

    def encode(self, strs: List[str]) -> str:
        output =""
        for i in strs:
            output += str(len(i))
            output += "#"
            output += i

        return output
        

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []

        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            output.append(s[j+1:j+1+n])
            i = j+n+1

        return output

