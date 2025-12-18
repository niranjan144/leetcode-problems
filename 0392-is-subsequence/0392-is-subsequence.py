class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=""
        j=0
        for i in t:
            if j < len(s) and i == s[j]:
                a += i
                j += 1
        if a==s:
            return(True)
        else:
            return(False)