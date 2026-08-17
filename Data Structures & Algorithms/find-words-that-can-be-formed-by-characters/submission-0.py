class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def makeHash(s):
            tmp= {}
            for letter in s:
                if letter in tmp:
                    tmp[letter] +=1
                else:
                    tmp[letter] = 1

            return tmp
        def canMakeFrom(m1,m2):
            for key, value in m1.items():
                if not (key in m2 and value <= m2[key]):
                    return False

            return True

        c = makeHash(chars)
        count =0
        for word in words:
            if canMakeFrom(makeHash(word),c):
                count+=len(word)

        return count
