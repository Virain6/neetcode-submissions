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
            length = "" 
            lengthNow = False

            while not lengthNow:
                if s[pointer] != ":":
                    length += s[pointer]
                else:
                    lengthNow = True
                pointer += 1

            output.append(s[pointer:pointer+int(length)])
            pointer += int(length)

        return output

        # Time: O(n), Space: O(n)


        