class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        maxi = 0

        for r in range(len(s)):
            char = s[r]

            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char] + 1

            last_seen[char] = r
            maxi = max(maxi, r - l + 1)

        return maxi

    def getHash(self, s):
        final = {}

        for letter in s:
            if final.get(letter) is None:
                final[letter] = 1
            else:
                final[letter] += 1

        return final

    def doesContainTHASH(self, s_hash):
        for key, value in self.t_hash.items():
            if key not in s_hash or s_hash[key] < value:
                return False

        return True

    def safeSkipLetter(self, letter, s_hash):
        if letter not in self.t_hash:
            return True

        return s_hash.get(letter, 0) > self.t_hash[letter]

    def minWindow(self, s: str, t: str) -> str:
        self.t_hash = self.getHash(t)

        if not self.doesContainTHASH(self.getHash(s)):
            return ""

        l = 0
        s_hash = {}
        final = ""

        for r in range(len(s)):
            right_letter = s[r]
            s_hash[right_letter] = s_hash.get(right_letter, 0) + 1

            # Shrink the current valid window from the left
            while self.doesContainTHASH(s_hash):
                current = s[l:r + 1]

                if final == "" or len(current) < len(final):
                    final = current

                left_letter = s[l]

                if self.safeSkipLetter(left_letter, s_hash):
                    s_hash[left_letter] -= 1

                    if s_hash[left_letter] == 0:
                        del s_hash[left_letter]

                    l += 1
                else:
                    break

        return final