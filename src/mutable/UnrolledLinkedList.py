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
        self._insert(self.tail, self.tail.node_size, element)
        return self

    def to_list(self):
        res = []
        node = self.head
        while node is not None:
            for ele in node.elements[0:node.node_size]:
                res.append(ele)
            node = node.next
        return res

    def from_list(self, lst):
        if len(lst) > 0:
            for e in lst:
                self.add(e)
        return self

    def remove(self, value):
        node = self.head
        while node is not None:
            index = 0
            for ele in node.elements[0:node.node_size]:
                if ele == value:
                    self._remove_from_node(node, index)
                index += 1
            node = node.next
        return self

    def reverse(self):
        lst = self.to_list()
        for ele in lst:
            self.remove(ele)
        lst.reverse()
        return self.from_list(lst)

    def _remove_from_node(self, node, index):
        if node.node_size == 1:
            if node.previous is not None:
                node.previous.next = node.next
            if node.next is not None:
                node.next.previous = node.previous
            node.next = None
            node.previous = None
            node.elements[index] = None
            node.node_size -= 1
            self.total_size -= 1
        else:
            for i in range(index, node.node_size-1):
                node.elements[i] = node.elements[i+1]
            node.node_size -= 1
            self.total_size -= 1

    def _insert(self, node, position, element):
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





