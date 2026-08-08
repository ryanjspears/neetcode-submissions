class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i, letter in enumerate(s):
            if i == len(s) - 1:
                continue
            
            count += abs(ord(letter) - ord(s[i+1]))

        return count
