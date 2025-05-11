import unittest
from problems.multiples_of_3_or_5.solution import solution_formula, solution_loop


class TestMultiplesOf3Or5(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(solution_formula(10), 23)
        self.assertEqual(solution_loop(10), 23)

    def test_negative_input(self):
        self.assertEqual(solution_formula(-5), 0)
        self.assertEqual(solution_loop(-5), 0)

    def test_zero_input(self):
        self.assertEqual(solution_formula(0), 0)
        self.assertEqual(solution_loop(0), 0)


if __name__ == "__main__":
    unittest.main()