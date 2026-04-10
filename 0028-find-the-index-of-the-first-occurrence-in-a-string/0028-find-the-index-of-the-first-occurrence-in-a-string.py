class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(n * m)
        # n: length of haystack
        # m: length of needle
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
