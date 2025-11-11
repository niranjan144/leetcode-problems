from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=[]
        for i in edges:
            for j in i:
                a.append(j)
        b=Counter(a)
        for val,key in b.items():
            if key>1:
                return(val)