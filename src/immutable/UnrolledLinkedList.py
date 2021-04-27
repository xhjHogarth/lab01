import copy


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


def size(node: Node) -> int:
    """
    Get the number of element in the UnrolledLinkedList.
    :param node: The head node of the UnrolledLinkedList.
    :return: The number of element in UnrolledLinkedList.
    """
    if node is None:
        return 0
    else:
        res = 0
        while node is not None:
            res += node.node_size
            node = node.next
        return res


def getter(node: Node, index: int):
    """
    Get the elements in the UnrolledLinkedList according to the index.
    :param node: The head node of the UnrolledLinkedList.
    :param index: The index of the element in the UnrolledLinkedList.(0 <= index < size)
    :return: If index is illegal, will through IndexError; otherwise,
    will return the element which is in the UnrolledLinkedList。
    """
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


def setter(node: Node, index: int, value) -> Node:
    """
    Update the element's value in the UnrolledLinkedList according to the index
    :param node: The head node of the UnrolledLinkedList.
    :param index: The index of the element in the UnrolledLinkedList.(0 <= index < size)
    :param value: The value of the element replacement in the UnrolledLinkedList.
    :return: If index is illegal, will through IndexError; otherwise, will return self.
    """
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


def cons(node: Node, value) -> Node:
    """
    Add an element into the UnrolledLinkedList.(element can be str,integer,None..).If the array is already full,
    we first insert a new node either preceding or following the current one and move half of the elements in
    the current node into it.
    :param node: The head node of the UnrolledLinkedList.
    :param value: The element add to UnrolledLinkedList.
    :return: self
    """
    if node is None:
        node = Node(5)
        node.elements[0] = value
        node.node_size = 1
    else:
        tmp = node
        while tmp.next is not None:
            tmp = tmp.next
        if tmp.node_size == tmp.capacity:
            new_node = Node(tmp.capacity)
            element_to_move = tmp.node_size // 2
            start_index = tmp.capacity - element_to_move
            i = 0
            for ele in tmp.elements[start_index:]:
                new_node.elements[i] = ele
                tmp.elements[start_index + i] = None
                i += 1
            new_node.elements[element_to_move] = value
            tmp.node_size -= element_to_move
            new_node.node_size = element_to_move + 1
            tmp.next = new_node
            new_node.previous = tmp
        else:
            tmp.elements[tmp.node_size] = value
            tmp.node_size += 1
    return node


def remove(node: Node, index: int) -> Node:
    """
    Remove element of the specific index in the UnrolledLinkedList.
    :param node: The head node of the UnrolledLinkedList.
    :param index: The index of the deleted element.
    :return: If index is not exist, will raise IndexError; otherwise, we will remove element and return self
    """
    self = node
    total_size = size(node)
    if 0 <= index < total_size:
        tag = 0
        while tag <= index:
            while node.node_size+tag-1 < index:
                tag += node.node_size
                node = node.next
            for i in range(0, node.node_size):
                if tag == index:
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
                tag += 1
        return self
    else:
        raise IndexError


def to_list(node: Node) -> list:
    """
    Get all the elements in the UnrolledLinkedList and convert them to the linked list to return.
    :param node: The head node of the UnrolledLinkedList.
    :return: List which contains all the elements in the UnrolledLinkedList.
    """
    res = []
    while node is not None:
        res += node.elements[0:node.node_size]
        node = node.next
    return res


def from_list(lst: list) -> Node:
    """
    Convert list to UnrolledLinkedList. If present obj is not None and contains elements, obj will initialization,
    and remove elements which already exists.
    :param lst: The list which convert to UnrolledLinkedList.
    :return: If param lst is not a instance of list, will raise TypeError; otherwise, will return self.
    """
    if not isinstance(lst, list):
        raise TypeError
    node = Node(5)
    self = node
    for item in lst:
        if node.next is not None:
            node = node.next
        cons(node, item)
    return self


def reverse(node: Node) -> Node:
    """
    Reverse the elements in the linked list. Firstly, Convert UnrolledLinkedList to list, and reverse it; then,
    convert list to UnrolledLinkedList.
    :param node: The head node of the UnrolledLinkedList.
    :return: self
    """
    lst = to_list(node)
    list.reverse(lst)
    return from_list(lst)


def mconcat(a: Node, b: Node) -> Node:
    """
    Concatenate node a and node b.
    :param a: node a
    :param b: node b
    :return: If param lst is not instance of UnrolledLinkedList,will raise TypeError; otherwise,
    concatenate self and lst, and return self.
    """
    if a is None:
        return b
    if b is None:
        return a
    if a.next is None and a.node_size == 0:
        return b
    if b.next is None and b.node_size == 0:
        return a

    c = copy.deepcopy(a)
    d = copy.deepcopy(b)

    res = c
    tail = c
    while c is not None:
        if c.next is None:
            tail = c
        c = c.next
    tail.next = d
    return res


def map(node: Node, f) -> Node:
    """
    Perform a specific function on the elements in the UnrolledLinkedList.
    :param node: The head node of the UnrolledLinkedList.
    :param f: Specific function
    :return: self(after execute specific function on the elements in the UnrolledLinkedList)
    """
    self = node
    while node is not None:
        for i in range(0, node.node_size):
            node.elements[i] = f(node.elements[i])
        node = node.next
    return self


def reduce(node: Node, f, initial_state) -> Node:
    state = initial_state
    while node is not None:
        for i in range(0, node.node_size):
            state = f(state, node.elements[i])
        node = node.next
    return state


def find(node: Node, value) -> bool:
    """
    Find the specific element in UnrolledLinkedList which val is equal to param value.
    :param node: The head node of the UnrolledLinkedList.
    :param value: specific value
    :return: True, if value is exist; False, if value is not exist.
    """
    while node is not None:
        for i in range(0, node.node_size):
            if node.elements[i] == value:
                return True
        node = node.next
    return False


def iterator(node: Node):
    """
    Iterator
    :param node: The head node of the UnrolledLinkedList.
    :return: iterator
    """
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


def filter(node: Node, f):
    """
    Filter the data in the UnrolledLinkedList.
    :param node: The head node of the UnrolledLinkedList.
    :param f: specific function
    :return: self
    """
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
