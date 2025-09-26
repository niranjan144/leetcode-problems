class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=[]
        sum2=[]
        c=0
        n=len(mat)
        m=n-1
        if n%2!=0:
            c=int(n/2)
        for i in range(0,n):
            for j in range(0,n):
                if i==j:
                    sum1.append(mat[i][j])
                else:
                    continue
        matr=mat[::-1]
        for i in range(0,n):
            for j in range(0,n):
                if i==j:
                    sum2.append(matr[i][j])
                else:
                        continue
        if n%2!=0:
            sum2.pop(c)
        a=sum1+sum2
        return(sum(a))