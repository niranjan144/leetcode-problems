class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if i<target:
                continue
            else:
                c+=1
        return c