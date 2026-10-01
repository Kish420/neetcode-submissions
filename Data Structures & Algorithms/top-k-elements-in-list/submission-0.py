class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for i, n in count.items():
            print(f"{i},{n}")
            freq[n].append(i)

        output = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                output.append(j)
                print(len(output) == k)
                if len(output) == k:
                    return output

        