class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=f"{x}"
        return st==st[::-1]
      
