class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in seen.items():
            buckets[freq].append(num)
        
        output = []

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output
            