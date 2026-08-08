class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums
        self.pos = len(nums) - k
        

    def add(self, val: int) -> int:
        #insert sort
        p = 0
        self.pos += 1
        print(self.heap)
        for i in range(len(self.heap)):
            if val < self.heap[i]:
                self.heap.insert(i, val)
                return self.heap[self.pos] 
        self.heap.append(val)
        return self.heap[self.pos]
        