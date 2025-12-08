from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        num,count = a.most_common(1)[0]
        return num