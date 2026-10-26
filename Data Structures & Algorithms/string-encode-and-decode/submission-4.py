class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for st in strs:
            output += str(len(st))+":"+st
        return output

        # Time: O(n), Space: O(n)

    def decode(self, s: str) -> List[str]:
        length = "" 
        lengthNow = False
        pointer = 0
        output=[]

        while pointer < len(s):
            while lengthNow == False:
                if s[pointer] != ":":
                    length += s[pointer]
                else:
                    lengthNow = True
                pointer += 1
            if length == "0":
                output.append("")
                lengthNow = False
                length = ""
            else:
                output.append(s[pointer:pointer+int(length)])
                pointer += int(length)
                lengthNow = False
                length = ""

        return output

        # Time: O(n), Space: O(n)


        