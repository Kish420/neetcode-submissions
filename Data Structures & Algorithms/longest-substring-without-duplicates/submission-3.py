class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        checked = {}

        while r < len(s):

            if s[r] in checked:
                if checked[s[l]] == l:
                    checked.pop(s[l])
                l += 1
                if l>r:
                    r = l
                    checked[s[r]] = r
            else:
                res = max(res, r - l+1)
                checked[s[r]] = r
                r += 1
        return res




        