class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def split_word(start: int) -> bool:
            # We successfully reached the end of the string.
            if start == len(s):
                return True

            # Return the previously calculated result.
            if start in memo:
                return memo[start]

            # Try every possible substring starting at this index.
            for end in range(start + 1, len(s) + 1):
                current_word = s[start:end]

                if current_word in words:
                    if split_word(end):
                        memo[start] = True
                        return True

            # This section of the string cannot be fully split.
            memo[start] = False
            return False

        return split_word(0)