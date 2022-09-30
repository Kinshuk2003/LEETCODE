class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            c=0
            for i in items:
                if i[0] == ruleValue:
                    c +=1
        elif ruleKey == "color":
            c=0
            for i in items:
                if i[1] == ruleValue:
                    c +=1
        elif ruleKey == "name":
            c=0
            for i in items:
                if i[2] == ruleValue:
                    c +=1
        return c
