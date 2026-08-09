class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def buildHash(word):
            m = {}

            for letter in word:
                if letter in m:
                    m[letter] += 1
                else:
                    m[letter] = 1
            
            return m

        
        ran, mag = buildHash(ransomNote), buildHash(magazine)

        for key, value in ran.items():
            if mag.get(key) is None:
                return False
            if mag[key] < value:
                return False


        return True 

        