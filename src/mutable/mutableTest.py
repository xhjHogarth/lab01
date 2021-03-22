import unittest

from hypothesis import given
import hypothesis.strategies as st

from mutable.mutable import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        self.assertRaises(UnrolledLinkedList(5), 0)


if __name__ == '__main__':
    unittest.main()
