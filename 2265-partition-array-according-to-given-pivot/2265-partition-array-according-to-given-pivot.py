class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        large=[]
        for i in nums:
            if i<=pivot:
                small.append(i)
            else:
                large.append(i)
        small.sort(key=lambda x: x == pivot)
        res=small+large
        return res