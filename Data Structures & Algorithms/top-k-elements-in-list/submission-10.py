class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        res = [[] for i in range(len(nums)+1)]
        output = []
        count = defaultdict(int)


        for n in nums:
            count[n] += 1

        for n, freq in count.items():
            res[freq].append(n)

        for i in range(len(res)-1, -1,-1):
            for j in res[i]:
                output.append(j)
                if len(output)==k:
                    return output




        