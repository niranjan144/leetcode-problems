class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000}
        count=0
        for i in range(len(s)):
            a=roman[s[i]]
            if i+1 < len(s):
                nv=roman[s[i+1]] 
            else:
                nv=0
            if a<nv:
                count-=a
            else:
                count+=a
        return count