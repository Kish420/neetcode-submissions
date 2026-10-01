class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        c = defaultdict(int)
        res = []

        for i in nums:
            c[i] += 1

        for i in c:
            freq[c[i]].append(i)

        for i in range(len(nums), 0 , -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        