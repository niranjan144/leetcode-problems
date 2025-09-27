class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=[]
        a=""
        n=dict(zip(indices,s))
        for i in range(len(s)):
            a=a+n[i]
        return a