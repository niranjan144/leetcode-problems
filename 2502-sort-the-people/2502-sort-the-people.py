class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=[]
        hn=dict(zip(heights,names))
        shn=sorted(heights)
        shn.reverse()
        for h in shn:
            a.append(hn[h])
        return(a)