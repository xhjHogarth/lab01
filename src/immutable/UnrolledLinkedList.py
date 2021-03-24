class Node:
    def __init__(self, capacity):
        self.node_size = 0
        self.capacity = capacity
        self.elements = [None] * capacity
        self.next = None
        self.previous = None

    def __eq__(self, other):
        """for write assertion. we should be abel for check list equality"""
        if other is None:
            return False
        if self.node_size != other.node_size:
            return False
        for i in range(0, self.node_size):
            if self.elements[i] != other.elements[i]:
                return False
        return self.next == other.next


def size(node):
    if node is None:
        return 0
    else:
        res = 0
        while node is not None:
            res += node.node_size
            node = node.next
        return res


def getter(node, index):
    total_size = size(node)
    if 0 <= index < total_size:
        i = 0
        while i <= index:
            for ele in node.elements[0:node.node_size]:
                if i == index:
                    return ele
                i += 1
            node = node.next
    else:
        raise IndexError


def setter(node, index, value):
    self = node
    total_size = size(node)
    if 0 <= index < total_size:
        i = 0
        while i <= index:
            for ele in node.elements[0:node.node_size]:
                if i == index:
                    node.elements[i] = value
                i += 1
            node = node.next
        return self
    else:
        raise IndexError


def cons(node, value):
    if node is None:
        node = Node(5)
        node.elements[0] = value
        node.node_size = 1
    else:
        if node.node_size == node.capacity:
            new_node = Node(node.capacity)
            element_to_move = node.node_size // 2
            start_index = node.capacity - element_to_move
            i = 0
            for ele in node.elements[start_index:]:
                new_node.elements[i] = ele
                node.elements[start_index + i] = None
                i += 1
            new_node.elements[element_to_move] = value
            node.node_size -= element_to_move
            new_node.node_size = element_to_move + 1
            node.next = new_node
            new_node.previous = node
        else:
            node.elements[node.node_size] = value
            node.node_size += 1
    return node


def remove(node, index):
    self = node
    total_size = size(node)
    if 0 <= index < total_size:
        i = 0
        while i <= index:
            for i in range(0, node.node_size):
                if i == index:
                    if node.node_size == 1:
                        if node.previous is not None:
                            node.previous.next = node.next
                        if node.next is not None:
                            node.next.previous = node.previous
                        node.next = None
                        node.previous = None
                        node.node_size = 0
                    else:
                        node.elements[i] = None
                        for j in range(i, node.node_size-1):
                            node.elements[j] = node.elements[j + 1]
                        node.node_size -= 1
                i += 1
            node = node.next
        return self
    else:
        raise IndexError


def to_list(node):
    res = []
    while node is not None:
        res += node.elements[0:node.node_size]
        node = node.next
    return res


def from_list(lst):
    node = Node(5)
    for item in lst:
        cons(node, item)
    return node


def reverse(node):
    lst = to_list(node)
    list.reverse(lst)
    return from_list(lst)


def mconcat(a, b):
    res = None
    if a is None:
        res = b
    if b is None:
        res = a

    res = a
    tail = a
    while a is not None:
        if a.next is None:
            tail = a
        a = a.next
    while b is not None:
        tail.next = b
        b = b.next
    return res


def map(node, f):
    self = node
    while node is not None:
        for i in range(0, node.node_size):
            node.elements[i] = f(node.elements[i])
        node = node.next
    return self


def reduce(node, f, initial_state):
    state = initial_state
    while node is not None:
        for i in range(0, node.node_size):
            state = f(state, node.elements[i])
        node = node.next
    return state


def find(node, value):
    while node is not None:
        for i in range(0, node.node_size):
            if node.elements[i] == value:
                return True
        node = node.next
    return False


def iterator(node):
    cur = node
    index = 0

    def foo():
        nonlocal cur
        nonlocal index
        if cur is None:
            raise StopIteration
        tmp = cur.elements[index]
        index += 1
        if index == cur.node_size:
            cur = cur.next
            index = 0
        return tmp

    return foo


def filter(node, f):
    lst = []
    try:
        get_next = iterator(node)
        while True:
            tmp = get_next()
            if f(tmp):
                lst.append(tmp)
    except StopIteration:
        pass
    return from_list(lst)


def mempty():
    return None
