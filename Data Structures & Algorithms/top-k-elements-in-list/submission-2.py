class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequencies for all the nums
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        # Bucket sort by frequency
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in seen.items():
            buckets[freq].append(num)

        # Return k highest 
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        output = []

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                output.append(num)

                if len(output) == k:
                    return output

        return output

# Time complexity = 3(O(n)) = O(n)
# Space complexity = 3(O(n)) = O(n)

