class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1]*length

        leftprod = 1
        for x in range(0, length):
            output[x] = leftprod
            leftprod *= nums[x]

        rightprod = 1
        for x in range(length-1, -1, -1):
            output[x] *= rightprod
            rightprod *= nums[x]
        
        return output