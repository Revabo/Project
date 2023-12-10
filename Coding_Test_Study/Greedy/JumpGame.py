##https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Max = 0
        i = 0

        while i < (Max+1):
          Max = max(Max, i + nums[i])
          if Max+1 >= len(nums):
            return True
          i += 1

        return False