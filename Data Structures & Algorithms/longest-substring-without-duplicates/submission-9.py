class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        maxi = 0

        for r in range(len(s)):
            char = s[r]

            # Only move left if the duplicate is inside the current window
            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char] + 1

            last_seen[char] = r
            maxi = max(maxi, r - l + 1)

        return maxi