class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for st in strs:
            key = [0]*26
            for c in st:
                key[ord(c) - 97] += 1

            seen[tuple(key)].append(st)
        return list(seen.values())
