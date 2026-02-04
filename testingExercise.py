# Write 2 tests that assert whether a list of integers and strings work with this function
# Part 2
# Go to this link https://gitlab.com/qacdevops/python-testing/-/tree/unit-testing-exercise
# And write tests for the 3 Python files.

import unittest


def count(sequence, item):
   sum = 0
   for n in sequence:
     if n == item:
        sum += 1
   return sum

class TestCountFunction(unittest.TestCase):

    def test_count_integers(self):
        self.assertEqual(count([1, 2, 3, 1, 1], 1), 3)
        self.assertEqual(count([1, 2, 3, 4], 5), 0)
        self.assertEqual(count([], 1), 0)

    def test_count_strings(self):
        self.assertEqual(count(['a', 'b', 'c', 'a'], 'a'), 2)
        self.assertEqual(count(['a', 'b', 'c'], 'd'), 0)
        self.assertEqual(count([], 'a'), 0)

if __name__ == '__main__':
    unittest.main()