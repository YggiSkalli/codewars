# tests/test_spin_words.py
import unittest
from codewars.problems.spin_words.spin_words import spin_words

class TestSpinWords(unittest.TestCase):
    """Test cases for the spin_words function."""

    def test_basic_cases(self):
        """Test basic functionality with typical inputs."""
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This is a test"), "This is a test")
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")

    def test_single_word(self):
        """Test single-word inputs."""
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("Hi"), "Hi")

    def test_edge_cases(self):
        """Test edge cases like empty strings and multiple spaces."""
        self.assertEqual(spin_words(""), "")
        self.assertEqual(spin_words("  Hey  "), "Hey")  # split() handles extra spaces

    def test_long_words(self):
        """Test inputs with multiple long words."""
        self.assertEqual(spin_words("fellow warriors another"), "wollef sroirraw rehtona")

    def test_alternative_solution(self):
        """Test the alternative generator-based solution."""
        from codewars.problems.spin_words.spin_words import spin_words_generator
        self.assertEqual(spin_words_generator("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words_generator("This is a test"), "This is a test")
        self.assertEqual(spin_words_generator("This is another test"), "This is rehtona test")
        
    

if __name__ == "__main__":
    unittest.main()