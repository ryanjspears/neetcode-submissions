class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for l in digits:
            s+=str(l)
        num = int(s)
        num+=1

        tmp = str(num)
        final  = []
        for l in list(tmp):
            final.append(int(l))

        return final
        