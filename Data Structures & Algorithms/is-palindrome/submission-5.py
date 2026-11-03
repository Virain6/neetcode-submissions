class Solution:
    def isPalindrome(self, s: str) -> bool:
         length = len(s) 

         ptrL = 0 
         ptrR = length - 1
         
         while ptrL <= ptrR:
            while ptrL < ptrR and not s[ptrL].isalnum():
                ptrL += 1
            while ptrR > ptrL and not s[ptrR].isalnum():
                ptrR -= 1
            
            if s[ptrL].isalnum() and s[ptrR].isalnum() and s[ptrL].lower() != s[ptrR].lower():
                return False
            
            ptrL += 1
            ptrR -= 1
         return True
#Time: O(n), Space O(1)