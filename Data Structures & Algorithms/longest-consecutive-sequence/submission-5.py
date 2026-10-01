class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in numSet:
            if (i - 1) not in numSet:
                total = 0
                while (i+total) in numSet:
                    total += 1
                longest = max(longest, total)

        return longest

            
            
        