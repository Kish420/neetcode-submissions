class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Smap = defaultdict(int)
        Tmap = defaultdict(int)

        for i in range(len(s)):
            Smap[s[i]] += 1
            Tmap[t[i]] += 1


        return Smap == Tmap


        
        