class Solution:
    def isPalindrome(self, s: str) -> bool:
         length = len(s) 

         ptrL = 0 
         ptrR = length - 1
         
         while ptrL <= ptrR:
            while ptrL < length-1 and not s[ptrL].isalnum():
                ptrL += 1
            while ptrR > 0 and not s[ptrR].isalnum():
                ptrR -= 1
            
            if s[ptrL].isalnum() and s[ptrR].isalnum() and s[ptrL].lower() != s[ptrR].lower():
                return False
            
            ptrL += 1
            ptrR -= 1
         return True