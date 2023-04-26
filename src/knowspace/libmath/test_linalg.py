import unittest
import time
from knowspace.libmath.linalg import Vector


class TestVector(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(Vector(1, 2, 3).dimension, 3)

    def test_add(self):
        self.assertEqual(Vector(1, 2, 3).plus(Vector(3, 4, 3)).elements, (4, 6, 6))
