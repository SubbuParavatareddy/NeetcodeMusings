class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <=0:
            return ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity        

    def get(self, i: int) -> int:
        if i <0 or i >= self.length:
            raise IndexError(f"Index {i} out of bounds (size: {self.length}")
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i <0 or i >= self.length:
            raise IndexError(f"Index {i} out of bounds (size: {self.length}")        
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.length == self.capacity):
            self.resize()        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("Cannot pop from Empty array")
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        new_arr[:self.length] = self.arr[:self.length]
        self.arr = new_arr

    def getSize(self) -> int:
          return self.length
    
    def getCapacity(self) -> int:
        return self.capacity