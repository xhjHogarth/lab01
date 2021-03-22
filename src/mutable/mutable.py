class Node:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.elements = [None] * capacity
        self.next = None
        self.previous = None


class UnrolledLinkedList:
    def __init__(self, capacity):
        assert capacity > 0, "capacity must set"
        self.size = 0
        self.nodeCapacity = capacity
        node = Node(capacity)
        self.head = node
        self.tail = self.head

    def size(self):
        return self.size


