class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
                ')': '(',
                '}': '{',
                ']': '['
            }


        for i in s:
            if i in p:
                if stack == [] or p[i] != stack.pop():
                    return False

            else:
                stack.append(i)

        return stack == []
        