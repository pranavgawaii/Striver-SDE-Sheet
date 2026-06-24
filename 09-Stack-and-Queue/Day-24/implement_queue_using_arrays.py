class Queue:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.front = 0
        self.rear = 0
        self.current_size = 0
        
    def push(self, x: int) -> None:
        if self.current_size == self.capacity:
            return
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.current_size += 1
        
    def pop(self) -> int:
        if self.current_size == 0:
            return -1
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.current_size -= 1
        return val
