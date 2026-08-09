class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0  # pointer for s
        j = 0  # pointer for t
        
        # Try to match as many characters of t in s as possible
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        
        # Characters from t that couldn't be matched
        return len(t) - j
