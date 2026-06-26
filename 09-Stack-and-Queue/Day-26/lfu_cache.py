class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def add_node(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        
    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
    def pop_tail(self) -> Node:
        if self.size > 0:
            node = self.tail.prev
            self.remove_node(node)
            return node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {}
        self.freq_list = {}
        
    def _update_freq(self, node: Node) -> None:
        freq = node.freq
        self.freq_list[freq].remove_node(node)
        
        if freq == self.min_freq and self.freq_list[freq].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        new_freq = node.freq
        
        if new_freq not in self.freq_list:
            self.freq_list[new_freq] = DoublyLinkedList()
            
        self.freq_list[new_freq].add_node(node)
        
    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
            
        node = self.key_node[key]
        self._update_freq(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_node) >= self.capacity:
                node_to_remove = self.freq_list[self.min_freq].pop_tail()
                del self.key_node[node_to_remove.key]
                
            new_node = Node(key, value)
            self.key_node[key] = new_node
            
            if 1 not in self.freq_list:
                self.freq_list[1] = DoublyLinkedList()
                
            self.freq_list[1].add_node(new_node)
            self.min_freq = 1
