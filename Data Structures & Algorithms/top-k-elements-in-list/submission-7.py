class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            count[n] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

        