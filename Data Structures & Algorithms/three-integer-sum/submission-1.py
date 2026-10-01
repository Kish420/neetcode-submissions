class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        checked = set()
        nums = sorted(nums)
        output = []

        for i, n in enumerate(nums):
            if n in checked:
                continue

            diff = 0 - n
            indexL = i + 1
            indexR = len(nums) - 1

            while indexL < indexR:
                num = nums[indexL] + nums[indexR]
                if num == diff:
                    result = [n, nums[indexL], nums[indexR]]
                    if result not in output:
                        output.append(result)
                    indexL += 1

                elif num < diff:
                    indexL += 1

                else:
                    indexR -= 1


            checked.add(n)
        return output


        
