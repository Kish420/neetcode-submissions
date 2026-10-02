class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        seen = set()

        for i in range(len(nums)):
            if nums[i] >0:
                break
            if nums[i] in seen:
                continue
            l, r = i+1, len(nums)-1
            while l<r and r<len(nums):
                if nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                if nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1

            seen.add(nums[i])

        return res






        