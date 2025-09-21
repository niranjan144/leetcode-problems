class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        while nums:
            maxa=max(nums)
            mina=min(nums)
            avg.append((mina+maxa)/2)
            nums.remove(maxa)
            nums.remove(mina)
        return(min(avg))