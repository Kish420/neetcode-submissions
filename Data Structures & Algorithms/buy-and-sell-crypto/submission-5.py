class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = 10000
        maxVal = 0
        profit = 0

        for n in prices:
            if n < minVal:
                minVal = n
                maxVal = 0
            
            else:
                maxVal = max(maxVal, n)
                profit = max(profit, maxVal-minVal)

            print(f"{maxVal}, {minVal}, {profit}")

        return profit

        