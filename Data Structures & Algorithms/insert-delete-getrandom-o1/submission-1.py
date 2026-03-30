from random import choice
class RandomizedSet:

    def __init__(self):
        self.nums_map = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
        self.nums_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_map:
            return False
        idx = self.nums_map[val]
        last = self.nums_list[-1]
        self.nums_list[idx] = last
        self.nums_map[last] = idx
        self.nums_list.pop()
        del self.nums_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()