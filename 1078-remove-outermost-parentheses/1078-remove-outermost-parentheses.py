class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=[]
        open=0
        for i in s:
            if i=='(' and open>0:
                a.append(i)
            if i==')' and open>1:
                a.append(i)
            if i=='(':
                open+=1
            else:
                open-=1
        return "".join(a)