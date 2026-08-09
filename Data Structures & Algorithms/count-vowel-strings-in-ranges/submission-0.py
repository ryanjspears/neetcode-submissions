class Solution:
    def vowelStrings(self, words, queries):
        vowels = set('aeiou')
        
        # Build prefix sum array
        prefix = [0]
        for word in words:
            starts_ends_vowel = int(word[0] in vowels and word[-1] in vowels)
            prefix.append(prefix[-1] + starts_ends_vowel)

        print(prefix)
        
        # Process queries
        result = []
        for l, r in queries:
            result.append(prefix[r+1] - prefix[l])
        
        return result