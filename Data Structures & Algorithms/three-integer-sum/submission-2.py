class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        checked = set()
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n in checked:
                continue

            l = i+1
            r = len(nums) - 1
            diff = 0 - n

            while l<r:
                num = nums[l] + nums[r]
                if num == diff:
                    output = [n, nums[l], nums[r]]
                    if output not in res:
                        res.append(output)
                    l += 1

                elif num < diff:
                    l += 1

                else:
                    r -= 1
        
        return res



        
