class MyHashSet:

    def __init__(self):
        self.h = {}
        

    def add(self, key: int) -> None:
        self.h[key] = True

        

    def remove(self, key: int) -> None:
        self.h[key] = False
        

    def contains(self, key: int) -> bool:
        if self.h.get(key) is None:
            return False

        tmp = self.h[key]

        return tmp


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)