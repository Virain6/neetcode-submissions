class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        leftProduct = 1
        for i in range(0, length):
            output[i] = leftProduct
            leftProduct *= nums[i]

        rightProduct = 1

        for i in range(length - 1, -1, -1):
            output[i] *= rightProduct
            rightProduct *= nums[i]
            
        return output
