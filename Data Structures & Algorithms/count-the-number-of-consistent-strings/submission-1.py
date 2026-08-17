class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m = set(list(allowed))
        count = 0
        for word in words:
            se = set(list(word))

            good = True
            for key in se:
                if  not key in m:
                    good = False
                    break
            
            if good:
                count+=1

        return count




