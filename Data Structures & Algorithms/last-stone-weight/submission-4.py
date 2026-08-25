class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        stones.sort()
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                one = stones.pop()
                two = stones.pop()
                stones.append(one - two)

            else:
                one = stones.pop()
                two = stones.pop()
                stones.append(two - one)

        if len(stones) == 0:
            return 0
        return stones.pop()
        