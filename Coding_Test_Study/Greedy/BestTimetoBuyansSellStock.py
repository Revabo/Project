##https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = -999
        min = 99999999
        for i in range(len(prices)):
          if min > prices[i]:
            min = prices[i]
          if ans < prices[i] - min:
              ans = prices[i] - min
        return ans