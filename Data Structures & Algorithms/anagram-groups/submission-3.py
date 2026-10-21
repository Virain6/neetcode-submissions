class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for st in strs:
            temp = [0]*26
            for s in st:
                temp[ord(s) - 97] += 1
            
            output[tuple(temp)].append(st)

        return list(output.values())

# Time Complexity: O(n*m) 
# n is the length of the array
# m is the max length of a string

# Space Complexity O(n)
# from the output dict