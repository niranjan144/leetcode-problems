class Solution:
    def numberOfSteps(self, num: int) -> int:
        a=num
        c=0
        while(a!=0):
            if a%2==0:
                a=a/2
                c+=1
            else:
                a=a-1
                c+=1
        return c