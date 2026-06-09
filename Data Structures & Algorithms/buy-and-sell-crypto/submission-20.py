class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(nums):
            if nums[l] < nums[r]:
                profit = max(profit, nums[r] - nums[l])
            else:
                l = r
            r += 1

        return profit 