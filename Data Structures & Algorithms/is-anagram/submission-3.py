class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}

        for c in s:
            hashmaps[c] = hashmaps.get(c, 0) + 1

        for c in t:
            hashmapt[c] = hashmapt.get(c, 0) + 1

        return hashmaps == hashmapt

# O(s+t) is the time complexity
# O(s+t) is the space complexity
    