class Node:
    def __init__(self, capacity):
        self.node_size = 0
        self.capacity = capacity
        self.elements = [None] * capacity
        self.next = None
        self.previous = None


class UnrolledLinkedList:
    def __init__(self, capacity):
        self.total_size = 0
        self.nodeCapacity = capacity
        node = Node(capacity)
        self.head = node
        self.tail = self.head

    def size(self):
        return self.total_size

    def add(self, element):
        self.insert(self.tail, self.tail.node_size, element)
        return self

    def insert(self, node, position, element):
        if node.node_size == self.nodeCapacity:
            new_node = Node(self.nodeCapacity)
            element_to_move = node.node_size//2
            start_index = self.nodeCapacity - element_to_move
            i = 0
            for ele in node.elements[start_index:]:
                new_node.elements[i] = ele
                node.elements[start_index+i] = None
                i += 1
            node.node_size -= element_to_move
            new_node.node_size = element_to_move

            new_node.next = node.next
            new_node.previous = node
            if node.next is not None:
                node.next.previous = new_node
            node.next = new_node
            if node is self.tail:
                self.tail = new_node

            if position > node.node_size:
                position -= node.node_size
                node = new_node
        i = node.node_size
        while True:
            if i <= position:
                break
            node.elements[i] = node.elements[i-1]
            i -= 1
        node.elements[position] = element
        node.node_size += 1
        self.total_size += 1





