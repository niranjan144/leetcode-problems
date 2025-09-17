class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        suml=0
        sumr=0
        n=len(nums)-1
        a=[]
        lr=[]
        diff=0
        left.append(0)
        right.append(0)
        for i in range(n):
            suml=suml+nums[i]
            left.append(suml)
        a=nums[::-1]
        for j in range(n):
            sumr=sumr+a[j]
            right.append(sumr)
        r=right[::-1]
        for k in range(len(left)):
            diff=abs(left[k]-r[k])
            lr.append(diff)
        return lr
