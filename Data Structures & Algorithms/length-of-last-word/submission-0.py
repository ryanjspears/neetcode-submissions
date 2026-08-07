class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0

        s = s.split(" ")
        return len(s[-1])
        