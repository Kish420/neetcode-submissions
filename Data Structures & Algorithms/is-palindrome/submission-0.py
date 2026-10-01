class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for i in s:
            if i.isalnum():
                string += (i.lower())

        print(string)

        return string == string[::-1]
        