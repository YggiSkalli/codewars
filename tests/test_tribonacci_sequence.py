
### Testdatei (`test_tribonacci_sequence.py`)

Hier ist eine Testdatei, die die Funktion `tribonacci` für verschiedene Fälle testet. Sie verwendet das `unittest`-Modul, das in Python eingebaut ist, und passt zu deinem GitHub-Setup.

```python
import unittest
from tribonacci_sequence import tribonacci, tribonacci_memoized

class TestTribonacciSequence(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(tribonacci([1, 1, 1], 8), [1, 1, 1, 3, 5, 9, 17, 31])
        self.assertEqual(tribonacci_memoized((1, 1, 1), 8), [1, 1, 1, 3, 5, 9, 17, 31])

    def test_n_equals_zero(self):
        self.assertEqual(tribonacci([1, 1, 1], 0), [])
        self.assertEqual(tribonacci_memoized((1, 1, 1), 0), [])

    def test_n_less_than_signature_length(self):
        self.assertEqual(tribonacci([1, 1, 1], 1), [1])
        self.assertEqual(tribonacci_memoized((1, 1, 1), 1), [1])

    def test_longer_signature(self):
        self.assertEqual(tribonacci([1, 2, 3, 4], 6), [1, 2, 3, 4, 9, 16])
        self.assertEqual(tribonacci_memoized((1, 2, 3, 4), 6), [1, 2, 3, 4, 9, 16])

    def test_short_signature(self):
        # Note: This may not align with Tribonacci rules (expects 3 elements)
        self.assertEqual(tribonacci([1, 1], 5), [1, 1, 2, 4, 7])
        self.assertEqual(tribonacci_memoized((1, 1), 5), [1, 1, 2, 4, 7])

if __name__ == '__main__':
    unittest.main()