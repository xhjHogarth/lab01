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

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        while self.count < self.total_size:
            value = self.get(self.count)
            self.count += 1
            return value
        raise StopIteration

    def get(self, index):
        if 0 <= index < self.total_size:
            i = 0
            node = self.head
            while i <= index:
                for ele in node.elements[0:node.node_size]:
                    if i == index:
                        return ele
                    i += 1
                node = node.next
        else:
            raise IndexError

    def set(self, index, value):
        if 0 <= index < self.total_size:
            i = 0
            node = self.head
            while i <= index:
                for ele in node.elements[0:node.node_size]:
                    if i == index:
                        node.elements[i] = value
                    i += 1
                node = node.next
            return self
        else:
            raise IndexError

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
        """if value is not exist, will raise ValueError"""
        node = self.head
        while node is not None:
            index = 0
            for ele in node.elements[0:node.node_size]:
                if ele == value:
                    self._remove_from_node(node, index)
                index += 1
            node = node.next
        if index == self.size():
            raise ValueError
        return self

    def reverse(self):
        lst = self.to_list()
        # This operation will take more time, when the linked list is very long
        # for ele in lst:
        #     self.remove(ele)
        self.total_size = 0
        self.head = Node(self.nodeCapacity)
        self.tail = self.head
        lst.reverse()
        return self.from_list(lst)

    def mconcat(self, lst):
        if lst is None:
            return self
        node = lst.head
        while node is not None:
            for i in range(0, node.node_size):
                self.add(node.elements[i])
            node = node.next
        return self

    def map(self, f):
        node = self.head
        while node is not None:
            for i in range(0, node.node_size):
                node.elements[i] = f(node.elements[i])
            node = node.next
        return self

    def reduce(self, f, initial_state):
        state = initial_state
        node = self.head
        while node is not None:
            for i in range(0, node.node_size):
                state = f(state, node.elements[i])
            node = node.next
        return state

    def find(self, value):
        return value in self

    def filter(self, f):
        event_list = list(filter(f, self.to_list()))

        # This operation will take more time, when the linked list is very long
        # for ele in self.to_list():
        #     self.remove(ele)

        self.total_size = 0
        self.head = Node(self.nodeCapacity)
        self.tail = self.head
        return self.from_list(event_list)

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
