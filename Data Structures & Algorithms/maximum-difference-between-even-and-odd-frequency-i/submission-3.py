class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = None
        max_even = None
        min_odd = None
        min_even = None
        l = {}
        for letter in s:
            if l.get(letter) is None:
                l[letter] = 1
            else:
                l[letter] += 1

        
        for key, value in l.items():
            if value % 2 == 0:
                if max_even is None:
                    max_even = key
                elif l[max_even] < value:
                    max_even = key

                if min_even is None:
                    min_even = key
                elif l[min_even] > value:
                    min_even = key
            else:
                if max_odd is None:
                    max_odd = key
                elif l[max_odd] < value:
                    max_odd = key
                
                if min_odd is None:
                    min_odd = key
                elif l[min_odd] < value:
                    min_odd = key

        return l[max_odd] - l[min_even]
            

        