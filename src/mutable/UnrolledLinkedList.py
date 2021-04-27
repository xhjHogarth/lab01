import copy

from immutable import UnrolledLinkedList


class Node:
    def __init__(self, capacity: int):
        """
        Initialization method
        :param capacity: the max elements that each node can store
        """
        self.node_size = 0
        self.capacity = capacity
        self.elements = [None] * capacity
        self.next = None
        self.previous = None


class UnrolledLinkedList:
    def __init__(self, capacity: int):
        """
        Initialization method
        :param capacity: The max elements that each node can store
        """
        self.total_size = 0
        self.nodeCapacity = capacity
        node = Node(capacity)
        self.head = node
        self.tail = self.head

    def __iter__(self):
        """
        Iterator
        :return: self
        """
        self.count = 0
        return self

    def __next__(self):
        """
        Get the next element
        :return: The next element before index reach size
        """
        while self.count < self.total_size:
            value = self.get(self.count)
            self.count += 1
            return value
        raise StopIteration

    def get(self, index: int) -> Node:
        """
        Get the elements in the UnrolledLinkedList according to the index.
        :param index: The index of the element in the UnrolledLinkedList.(0 <= index < size)
        :return: If index is illegal, will through IndexError; otherwise,
        will return the element which is in the UnrolledLinkedList。
        """
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

    def set(self, index: int, value) -> UnrolledLinkedList:
        """
        Update the element's value in the UnrolledLinkedList according to the index
        :param index: The index of the element in the UnrolledLinkedList.(0 <= index < size)
        :param value: The value of the element replacement in the UnrolledLinkedList.
        :return: If index is illegal, will through IndexError; otherwise, will return self.
        """
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

    def size(self) -> int:
        """
        Get the number of element in the UnrolledLinkedList.
        :return: The number of element in UnrolledLinkedList.
        """
        return self.total_size

    def add(self, element) -> UnrolledLinkedList:
        """
        Add an element into the UnrolledLinkedList.(element can be str,integer,None..).If the array is already full,
        we first insert a new node either preceding or following the current one and move half of the elements in
        the current node into it.
        :param element: The element add to UnrolledLinkedList.
        :return: self
        """
        self._insert(self.tail, self.tail.node_size, element)
        return self

    def to_list(self) -> list:
        """
        Get all the elements in the UnrolledLinkedList and convert them to the linked list to return.
        :return: List which contains all the elements in the UnrolledLinkedList.
        """
        res = []
        node = self.head
        while node is not None:
            for ele in node.elements[0:node.node_size]:
                res.append(ele)
            node = node.next
        return res

    def from_list(self, lst: list) -> UnrolledLinkedList:
        """
        Convert list to UnrolledLinkedList. If present obj is not None and contains elements, obj will initialization,
        and remove elements which already exists.
        :param lst: The list which convert to UnrolledLinkedList.
        :return: If param lst is not a instance of list, will raise TypeError; otherwise, will return self.
        """
        if not isinstance(lst, list):
            raise TypeError
        if self.size() > 0:
            node = self.head
            node.node_size = 0
            node.capacity = self.nodeCapacity
            node.elements = [None] * self.nodeCapacity
            node.next = None
            node.previous = None
            self.total_size = 0
            self.head = node
            self.tail = self.head
        if len(lst) > 0:
            for e in lst:
                self.add(e)
        return self

    def remove(self, value) -> UnrolledLinkedList:
        """
        Remove the specific value in the UnrolledLinkedList.
        :param value: The value that we want to remove.
        :return: If value is not exist, will raise ValueError; otherwise, we will remove element and return self
        """
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

    def reverse(self) -> UnrolledLinkedList:
        """
        Reverse the elements in the linked list. Firstly, Convert UnrolledLinkedList to list, and reverse it; then,
        convert list to UnrolledLinkedList.
        :return: self
        """
        lst = self.to_list()
        # This operation will take more time, when the linked list is very long
        # for ele in lst:
        #     self.remove(ele)
        self.total_size = 0
        self.head = Node(self.nodeCapacity)
        self.tail = self.head
        lst.reverse()
        return self.from_list(lst)

    def mconcat(self, lst: UnrolledLinkedList) -> UnrolledLinkedList:
        """
        Concatenate self and lst.
        :param lst: which will concatenate with self
        :return: If param lst is not instance of UnrolledLinkedList,will raise TypeError; otherwise,
        concatenate self and lst, and return self.
        """
        if lst is None:
            return self
        if not isinstance(lst, UnrolledLinkedList):
            raise TypeError
        tmp = copy.deepcopy(self)
        node = lst.head
        while node is not None:
            for i in range(0, node.node_size):
                tmp.add(node.elements[i])
            node = node.next
        return tmp

    def map(self, f) -> UnrolledLinkedList:
        """
        Perform a specific function on the elements in the UnrolledLinkedList.
        :param f: Specific function
        :return: self(after execute specific function on the elements in the UnrolledLinkedList)
        """
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

    def find(self, value) -> bool:
        """
        Find the specific element in UnrolledLinkedList which val is equal to param value.
        :param value: specific value
        :return: True, if value is exist; False, if value is not exist.
        """
        return value in self

    def filter(self, f) -> UnrolledLinkedList:
        """
        Filter the data in the UnrolledLinkedList.
        :param f: specific function
        :return: self
        """
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
