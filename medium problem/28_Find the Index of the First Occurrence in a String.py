class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None:
            return 0
        else:
            x=haystack.find(needle)
            return x
