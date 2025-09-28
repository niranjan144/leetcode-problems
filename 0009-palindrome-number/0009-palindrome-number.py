class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        rs=s[::-1]
        return(rs==s)