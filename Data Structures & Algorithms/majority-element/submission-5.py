class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prevMap = {}

        for num in nums:
            if num in prevMap:
                prevMap[num] += 1
            else:
                prevMap[num] = 1

            if prevMap[num] > len(nums)//2:
                return num