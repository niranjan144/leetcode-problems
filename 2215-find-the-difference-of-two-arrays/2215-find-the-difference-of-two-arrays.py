class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        num1=set(nums1)
        num2=set(nums2)
        for i in num1:
            if i not in num2:
                a.append(i)
        for j in num2:
            if j not in num1:
                b.append(j)
        return(a,b)