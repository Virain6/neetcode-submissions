class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            need = target - num
            val = seen.get(need)
            if val != None: 
                return [val, index]
            seen[num] = index

# Time Complexity: O(n) 
# Space Complexity: O(n)