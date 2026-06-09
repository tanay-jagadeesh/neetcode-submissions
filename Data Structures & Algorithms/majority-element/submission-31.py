class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prevMap = {}

        for num in nums: 
            prevMap[num] = prevMap.get(num, 0) + 1

            if prevMap[num] > len(nums) / 2: 
                return num
        