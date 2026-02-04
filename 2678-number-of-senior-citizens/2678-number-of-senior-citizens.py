class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age=[]
        count=0
        for i in details:
            age.append(i[11:13])
        for i in age:
            if int(i)>60:
                count+=1
        return(count)