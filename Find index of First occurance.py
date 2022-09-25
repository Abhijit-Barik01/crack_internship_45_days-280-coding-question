class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        win_size=len(needle)
        for i in range(0,len(haystack)):
            substring=haystack[i:win_size+i]
            if needle==substring:
                return i
        return -1
