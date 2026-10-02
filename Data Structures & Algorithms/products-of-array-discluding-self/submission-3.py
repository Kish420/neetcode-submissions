class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [[] for i in range(len(nums))]
        postfix = [[] for i in range(len(nums))]

        p = 1
        for i, n in enumerate(nums):
            prefix[i] = p = p*n

        p = 1
        for i in range(len(nums)-1, -1 ,-1):
            postfix[i] = p = p * nums[i]
        output = []

        for i in range(len(nums)):
            pre = prefix[i-1] if i>0 else 1
            post = postfix[i+1] if (i+1)<len(nums) else 1
            output.append(pre*post)

        return output
        