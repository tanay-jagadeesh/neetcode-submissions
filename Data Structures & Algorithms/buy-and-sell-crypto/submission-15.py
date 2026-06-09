class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(len(nums)):
            if nums[l] < nums[r]:
                profit = max(profit, nums[r] - nums[l])
            elif nums[l] > nums[r]: 
                l = r 
        return profit 