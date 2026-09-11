class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        prefix = ""
        for i in range(len(word)+1):
            cur = word[:i+1]
            good = True
            for item in strs:
                if cur != item[:i+1]:
                    return prefix
            
            prefix = cur

        return prefix
                

        