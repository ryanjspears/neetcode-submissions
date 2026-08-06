class Solution:
    def isPalindrome(
        self,
        s: str,
        left: int,
        right: int,
        memo: dict
    ) -> bool:
        key = (left, right)

        if key in memo:
            return memo[key]

        if left >= right:
            return True

        memo[key] = (
            s[left] == s[right]
            and self.isPalindrome(
                s,
                left + 1,
                right - 1,
                memo
            )
        )

        return memo[key]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        memo = {}
        n = len(s)

        while n > 0:
            left = 0
            right = n - 1

            for i in range(len(s) - n + 1):
                current_left = left + i
                current_right = right + i

                if self.isPalindrome(
                    s,
                    current_left,
                    current_right,
                    memo
                ):
                    return s[current_left:current_right + 1]

            n -= 1

        return ""