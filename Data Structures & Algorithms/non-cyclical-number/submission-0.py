class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        cur = n
        while not cur in visited:
            visited.add(cur)
            nums = list(str(cur))
            count = 0
            for num in nums:
                num = int(num)
                count += num**2
            if count == 1:
                return True
            
            cur = count

        return False


            

        