import unittest

from hypothesis import given
import hypothesis.strategies as st

from mutable.UnrolledLinkedList import *


class TestUnrolledLinkedList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(UnrolledLinkedList(5).size(), 0)
        self.assertEqual(UnrolledLinkedList(5).add(1).size(), 1)
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4)
                         .add(5).add(6).add(7).size(), 7)

    def test_add(self):
        self.assertEqual(UnrolledLinkedList(5).add(None).to_list(), [None])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(None).add("123").to_list(),
                         [1, 2, 3, 4, None, "123"])

    @given(st.lists(st.integers()))
    def test_add2(self, a):
        lst = UnrolledLinkedList(5)
        for item in a:
            lst.add(item)
        self.assertEqual(lst.to_list(), a)

    def test_to_list(self):
        self.assertEqual(UnrolledLinkedList(5).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).to_list(), [1, 2, 3])

    @given(st.lists(st.integers()))
    def test_to_list2(self, a):
        lst = UnrolledLinkedList(5)
        for item in a:
            lst.add(item)
        self.assertEqual(lst.to_list(), a)

    def test_from_list(self):
        test_data = [
            [],
            [1, 2],
            [1, 2, 3, 4, 5, 6, 7]
        ]
        for e in test_data:
            lst = UnrolledLinkedList(5).from_list(e)
            self.assertEqual(lst.to_list(), e)

    @given(st.lists(st.integers()))
    def test_from_list2(self, a):
        lst1 = UnrolledLinkedList(5)
        lst2 = UnrolledLinkedList(5)
        for item in a:
            lst2.add(item)
        self.assertEqual(lst1.from_list(a).to_list(), lst2.to_list())

    def test_remove(self):
        # self.assertEqual(UnrolledLinkedList(5).remove(1).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).remove(1).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4)
                         .add(5).add(6).add(7).remove(6).to_list(), [1, 2, 3, 4, 5, 7])
        self.assertRaises(ValueError, lambda: UnrolledLinkedList(5).add(1).add(2).add(3).add(4).remove(5))

    def test_reverse(self):
        self.assertEqual(UnrolledLinkedList(5).reverse().to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3)
                         .reverse().to_list(), [3, 2, 1])

    @given(st.lists(st.integers()))
    def test_reverse2(self, a):
        x = UnrolledLinkedList(5).from_list(a).reverse()
        self.assertEqual(x.to_list(), a[::-1])

    def test_map(self):
        lst = UnrolledLinkedList(5)
        lst.map(str)
        self.assertEqual(lst.to_list(), [])

        lst = UnrolledLinkedList(5)
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ['1', '2', '3'])

        lst = UnrolledLinkedList(5)
        lst.from_list([1, 2, 3])
        lst.map(lambda x: x + 1)
        self.assertEqual(lst.to_list(), [2, 3, 4])

    def test_reduce(self):
        lst = UnrolledLinkedList(5)
        self.assertEqual(lst.reduce(lambda state, e: state + e, 0), 0)
        self.assertEqual(lst.reduce(lambda state, e: state + e, 1), 1)

        lst = UnrolledLinkedList(5)
        lst.from_list([1, 2, 3, 4])
        self.assertEqual(lst.reduce(lambda state, e: state + e, 0), 10)

    def test_get(self):
        self.assertRaises(IndexError, lambda: UnrolledLinkedList(5).add(1).get(1))
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).get(2), 3)

    def test_iter(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(5).add(6).add(7)
        lst2 = []
        for n in lst:
            try:
                lst2.append(n)
            except StopIteration:
                pass
        self.assertEqual(lst2, [1, 2, 3, 4, 5, 6, 7])

    def test_mconcat(self):
        lst1 = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst2 = UnrolledLinkedList(5).add(4).add(5).add(6).add(7)
        lst1.mconcat(lst2)
        lst3 = UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(5).add(6).add(7)
        self.assertEqual(lst1.to_list(), lst3.to_list())

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst1):
        a = UnrolledLinkedList(5).from_list(lst1)
        b = UnrolledLinkedList(5).from_list([1, 2, 3, 4, 5, 0])
        self.assertEqual(a.mconcat(None), a)
        self.assertEqual(a.mconcat(b).to_list(), lst1+[1, 2, 3, 4, 5, 0])

    def test_find(self):
        lst = UnrolledLinkedList(5)
        self.assertEqual(lst.find(2), False)
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        self.assertEqual(lst.find(2), True)
        self.assertEqual(lst.find(4), False)

    def test_set(self):
        lst = UnrolledLinkedList(5)
        self.assertRaises(IndexError, lambda: lst.set(0, 1))
        lst.add(1).add(2).add(3).add(4)
        self.assertEqual(lst.set(1, 5).to_list(), [1, 5, 3, 4])

    def test_filter(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(5)

        def is_even(n):
            return n % 2 == 0
        self.assertEqual(lst.filter(is_even).to_list(), [2, 4])
        self.assertEqual(lst.filter(lambda x: x % 2 == 0).to_list(), [2, 4])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = UnrolledLinkedList(5)
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = UnrolledLinkedList(5)
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))


if __name__ == '__main__':
    unittest.main()
