class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=[]
        for i in sentences:
            a = i.split()
            m.append(len(a))
        return max(m)
