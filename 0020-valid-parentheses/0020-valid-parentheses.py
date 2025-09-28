class Solution:
    def isValid(self, s: str) -> bool:
        para={'(':')', '{':'}','[':']'}
        stack=[]
        for i in s:
            if i in para:
                stack.append(i)
            elif len(stack) == 0 or para[stack.pop()]!=i:
                return(False)
        return(len(stack)==0)