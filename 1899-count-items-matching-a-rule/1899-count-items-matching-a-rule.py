class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKey1 = "type"
        ruleKey2 = "color"
        ruleKey3 = "name"
        count=0
        if ruleKey==ruleKey1:
            rule=0
        else:
            if ruleKey==ruleKey2:
                rule=1
            else:
                if ruleKey==ruleKey3:
                    rule=2
        for i in items:
            if ruleValue==i[rule]:
                count+=1
        return count