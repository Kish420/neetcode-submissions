class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output += str(len(i))
            output += '#'
            output += i
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1

            l = int(s[i:j])
            output.append(s[j+1:j+l+1])
            i = j+l+1

        return output




