class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        lastVal = self.arr[-1]        
        i = self.set[val]
        self.set[lastVal] = i
        self.arr[i] = lastVal
        del self.set[val]        
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()