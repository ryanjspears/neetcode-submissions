# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n #2 5

        while l<=r:
            mid = ((r-l)//2) + l
            print(mid)

            if guess(mid) == 0:
                print("here")
                return mid
            
            if guess(mid) == -1:
                print("here2")
                r = mid - 1
            else:
                l = mid + 1

        return 0
        