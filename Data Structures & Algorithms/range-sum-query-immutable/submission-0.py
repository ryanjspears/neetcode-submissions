class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        

    def sumRange(self, left: int, right: int) -> int:
        count = 0
        while left <= right:
            count += self.arr[left]
            left += 1

        return count
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)