import unittest

from hypothesis import given
import hypothesis.strategies as st

from immutable.UnrolledLinkedList import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        node = Node(5)
        for i in range(0, 3):
            node.elements[i] = i + 1
            node.node_size += 1
        self.assertEqual(size(node), 3)

    def test_getter(self):
        self.assertRaises(IndexError, lambda: getter(Node(5), 1))
        node = Node(5)
        for i in range(0, 3):
            node.elements[i] = i + 1
            node.node_size += 1
        self.assertEqual(getter(node, 1), 2)

    def test_setter(self):
        self.assertRaises(IndexError, lambda: setter(Node(5), 1, 2))
        node = Node(5)
        for i in range(0, 3):
            node.elements[i] = i + 1
            node.node_size += 1
        self.assertEqual(to_list(setter(node, 1, 3)), [1, 3, 3])

    def test_cons(self):
        self.assertEqual(cons(None, 1), cons(Node(3), 1))
        self.assertEqual(to_list(cons(cons(cons(None, 1), 2), 3)), [1, 2, 3])
        self.assertEqual(to_list(cons(cons(cons(cons(cons(cons(None, 1), 2), 3), 4), 5), 6)), [1, 2, 3, 4, 5, 6])

    def test_remove(self):
        self.assertRaises(IndexError, lambda: remove(cons(None, 1), 2))
        self.assertEqual(to_list(remove(cons(cons(cons(None, 1), 2), 3), 2)), [1, 2])

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(cons(cons(cons(None, 1), 2), 3)), [1, 2, 3])

    def test_from_list(self):
        self.assertEqual(from_list([]), Node(5))
        node = Node(5)
        for i in range(0, 3):
            node.elements[i] = i + 1
            node.node_size += 1
        self.assertEqual(from_list([1, 2, 3]), node)

    def test_reverse(self):
        self.assertEqual(reverse(Node(5)), Node(5))
        self.assertEqual(reverse(cons(cons(cons(None, 1), 2), 3)), cons(cons(cons(None, 3), 2), 1))

    def test_mconcat(self):
        self.assertEqual(mconcat(Node(5), None), Node(5))
        self.assertEqual(to_list(mconcat(cons(None, 1), cons(None, 2))), [1, 2])
        self.assertEqual(to_list(mconcat(cons(cons(cons(None, 1), 2), 3),
                                         cons(cons(cons(None, 4), 5), 6))), [1, 2, 3, 4, 5, 6])

    def test_map(self):
        self.assertEqual(to_list(map(Node(5), str)), [])
        self.assertEqual(to_list(map(cons(cons(cons(None, 1), 2), 3), str)), ['1', '2', '3'])
        self.assertEqual(to_list(map(cons(cons(cons(None, 1), 2), 3), lambda x: x+1)), [2, 3, 4])

    def test_reduce(self):
        self.assertEqual(reduce(Node(5), lambda state, e: state + e, 0), 0)
        self.assertEqual(reduce(Node(5), lambda state, e: state + e, 1), 1)
        self.assertEqual(reduce(cons(cons(cons(None, 1), 2), 3), lambda state, e: state + e, 0), 6)

    def test_find(self):
        self.assertEqual(find(Node(5), 1), False)
        self.assertEqual(find(cons(cons(cons(None, 1), 2), 3), 2), True)
        self.assertEqual(find(cons(cons(cons(cons(cons(cons(None, 1), 2), 3), 4), 5), 6), 5), True)

    def test_iterator(self):
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)

        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    def test_filter(self):
        def is_even(n):
            return n % 2 == 0
        self.assertEqual(filter(cons(cons(cons(cons(cons(cons(None, 1), 2), 3), 4), 5), 6), lambda x: is_even(x)),
                         cons(cons(cons(None, 2), 4), 6))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)


if __name__ == '__main__':
    unittest.main()
