import unittest

from hypothesis import given
import hypothesis.strategies as st

from mutable.UnrolledLinkedList import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        self.assertEqual(UnrolledLinkedList(5).size(), 0)
        self.assertEqual(UnrolledLinkedList(5).add(1).size(), 1)
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4)
                         .add(5).add(6).add(7).size(), 7)

    def test_to_list(self):
        self.assertEqual(UnrolledLinkedList(5).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).to_list(), [1, 2, 3])

    def test_from_list(self):
        test_data = [
            [],
            [1, 2],
            [1, 2, 3, 4, 5, 6, 7]
        ]
        for e in test_data:
            lst = UnrolledLinkedList(5).from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_remove(self):
        self.assertEqual(UnrolledLinkedList(5).remove(1).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).remove(1).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4)
                         .add(5).add(6).add(7).remove(6).to_list(), [1, 2, 3, 4, 5, 7])

    def test_reverse(self):
        self.assertEqual(UnrolledLinkedList(5).reverse().to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3)
                         .reverse().to_list(), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
