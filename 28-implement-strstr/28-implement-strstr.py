class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return -1
        else:
            try:
                x = haystack.index(needle)
                return x
            except Exception:
                return -1
        