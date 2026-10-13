"""06 - unittest, doctest, pdb tips."""
import unittest

def add(a, b):
    """Add two numbers.

    >>> add(2, 3)
    5
    """
    return a + b

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.vals = (2, 3)
    def test_add(self):
        self.assertEqual(add(*self.vals), 5)
    def test_raises(self):
        with self.assertRaises(TypeError):
            add(1, "x")

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    unittest.main(argv=["x"], exit=False, verbosity=1)

# Debugging tips:
#   breakpoint()                 # drops into pdb
#   python -m pdb script.py
#   python -X dev script.py      # extra runtime checks
#   python -m pytest -x -q       # see tests/ folder (pytest style)
