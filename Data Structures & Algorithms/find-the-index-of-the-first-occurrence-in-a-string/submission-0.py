class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)

        if n2 > n1:
            return -1

        p = 0

        while p + n2 <= n1:
            if haystack[p:p+n2] == needle:
                return p
            p+=1

        return -1

        