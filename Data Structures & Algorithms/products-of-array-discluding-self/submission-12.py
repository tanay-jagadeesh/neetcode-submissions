class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            ind = 1
            prefix = nums[ :i]
            postfix = nums[i+1: ]

            for num in prefix: 
                ind *= num
            
            for num in postfix: 
                ind *= num

            output.append(ind)
        return output
            
    