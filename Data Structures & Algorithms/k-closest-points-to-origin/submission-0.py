import heapq
class Solution:
    def diff(self, x, y):
        return (x**2 + y**2) ** 0.5
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            calc = self.diff(x,y)
            heapq.heappush(heap, (calc, [x,y]))
        final = []
        for i in range(k):
            d, cors = heapq.heappop(heap)
            x,y = cors
            final.append([x,y])
        
        return final
        