class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        prevMap = {}
        result = []

        for num in nums: 
            if num in prevMap:
                prevMap[num] +=1
            else:
                prevMap[num] = 1
        

            if prevMap[num] > len(nums)/3 and num not in result: 
                result.append(num)

                
        return result