class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y=[]
        y=[int(i) for i in str(x)]
        z=sum(y)
        if x%z==0:
            return(z)
        else:
            return(-1)