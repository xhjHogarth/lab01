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


if __name__ == '__main__':
    unittest.main()
