class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0
        length = 0
        arr_len = len(nums)
        
        for num in nums:
            if num-1 not in seen:
                length = 1
                while num+length in seen:
                    length += 1
                max_length = max(max_length, length)
                
                if max_length >= arr_len/2:
                    return max_length
        return max_length
    