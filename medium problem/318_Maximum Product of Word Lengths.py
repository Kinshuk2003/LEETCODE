class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_value=0
        char = [set(words[i]) for i in range(len(words))]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (char[i] & char[j]):
                    max_value=max(max_value,len(words[i])*len(words[j]))
        return max_value
