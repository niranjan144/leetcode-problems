class Solution:
    def countAsterisks(self, s: str) -> int:
        stk=""
        count=0
        co=0
        for i in s:
            if i=="|":
                count+=1
            if count%2==0:
                stk+=i
        for i in stk:
            if i=='*':
                co+=1
        return co