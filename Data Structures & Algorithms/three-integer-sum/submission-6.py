class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for index, num in enumerate(nums):
            low = index 
            high = len(nums) -1

            if nums[index-1] == num and num != 0:
                continue

            while low < high:
                if low == index:
                    low += 1
                
                if high == index:
                    high -= 1
                
                if low >= high:
                    break

                total = nums[low] + nums[high]
                if total == -num:
                    temp = [num, nums[low], nums[high]]
                    if temp not in output:
                        output.append(temp) 
                
                if total > -num:
                    high -= 1

                else:
                    low += 1 
        
        return output

# Time: O(n*n) = O(n^2)