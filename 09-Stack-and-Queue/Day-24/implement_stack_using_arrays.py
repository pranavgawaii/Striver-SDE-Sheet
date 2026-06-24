class Stack:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.top_index = -1
        
    def push(self, x: int) -> None:
        if self.top_index >= self.capacity - 1:
            return
        self.top_index += 1
        self.arr[self.top_index] = x
        
    def pop(self) -> int:
        if self.top_index < 0:
            return -1
        val = self.arr[self.top_index]
        self.top_index -= 1
        return val
        
    def top(self) -> int:
        if self.top_index < 0:
            return -1
        return self.arr[self.top_index]
        
    def is_empty(self) -> int:
        return 1 if self.top_index < 0 else 0
