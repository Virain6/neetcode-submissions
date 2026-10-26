class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for st in strs:
            output += str(len(st))+":"+st
        return output

        # Time: O(n), Space: O(n)

    def decode(self, s: str) -> List[str]:
        pointer = 0
        output=[]

        while pointer < len(s):
            # Find where the length ends
            start = pointer

            while s[pointer] != ":":
                pointer += 1

            # Extract the length
            length = int(s[start:pointer])

            # Move past the colon
            pointer += 1

            # Extract the original string
            output.append(s[pointer:pointer + length])

            # Move to the next encoded string
            pointer += length


        return output

        # Time: O(n), Space: O(n)


        