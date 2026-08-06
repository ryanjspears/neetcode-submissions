class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(current_s: str) -> int:
            # Already calculated how many ways this substring can be decoded.
            if current_s in memo:
                return memo[current_s]

            # The entire string was successfully split.
            if current_s == "":
                return 1

            # A number cannot begin with zero.
            if current_s[0] == "0":
                return 0

            count = 0

            # Split using the first single digit.
            one_digit = int(current_s[0])

            if 1 <= one_digit <= 26:
                count += decode(current_s[1:])

            # Split using the first two digits.
            if len(current_s) >= 2:
                two_digits = int(current_s[:2])

                if 1 <= two_digits <= 26:
                    count += decode(current_s[2:])

            memo[current_s] = count
            return count

        return decode(s)