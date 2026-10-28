class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        for i in range(1, length):
            output[i] = nums[i-1]*output[i-1]*output[i]

        rightProduct = 1

        for i in range(length - 1, -1, -1):
            output[i] *= rightProduct
            rightProduct *= nums[i]
            
        return output
