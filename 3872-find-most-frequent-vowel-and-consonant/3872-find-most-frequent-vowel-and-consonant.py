from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=set("aeiou")
        c=Counter(s)
        mv=[]
        mc=[]
        a=[]
        for i in v:
            if i in c:
                mv.append(c[i])
            else:
                mv.append(0)
        for i in c:
            if i not in v:
                mc.append(c[i])
            else:
                mc.append(0)
        m=max(mc)
        d=max(mv)
        n=m+d
        return n