class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        prevMap = {}
        result = []

        for num in nums: 
            prevMap[num] = 1 + prevMap.get(num, 0)

            if prevMap[num] > len(nums) / 3 and num not in result:
                result.append(num)
        return result
                