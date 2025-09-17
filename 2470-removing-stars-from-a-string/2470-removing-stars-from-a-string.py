class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in s:
            if i!="*":
                a.append(i)
            else:
                if a:
                    a.pop()
        return "".join(a)