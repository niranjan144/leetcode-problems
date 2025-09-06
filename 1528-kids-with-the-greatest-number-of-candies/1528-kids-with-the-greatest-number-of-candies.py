class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        a=[]
        for i in range(len(candies)):
            if ((candies[i] + extraCandies)>= maximum):
                a.append(True)
            else:
                a.append(False)
        return a