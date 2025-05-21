# Is Pangram

## Problem Description
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return `True` if it is, `False` if not. Ignore numbers and punctuation.

**Examples:**
- `"The quick brown fox jumps over the lazy dog"` → `True`
- `"Hello, World!"` → `False`

**Link to Problem:** [Codewars - Is a string a pangram?](https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python)

## Solution
The solution is implemented in Python with three different approaches:
1. **Short Solution (`is_pangram`)**: Uses a generator expression and set to check if the string contains all 26 letters in a single line.
2. **Long Solution (`is_pangram_long`)**: Breaks down the process into clear steps for better readability, using a list and set to collect unique letters.
3. **Subset Solution (`is_pangram_subset`)**: Checks if the alphabet is a subset of the string's letters using set operations.

Each solution ignores case, numbers, and punctuation as required.

## Approach
- Convert the input string to lowercase to make the check case-insensitive.
- Filter out non-alphabetic characters (numbers, punctuation, spaces).
- Use a set to collect unique letters and check if there are exactly 26 (the number of letters in the alphabet).
- Alternatively, compare the set of letters in the string against the full alphabet.

## Lessons Learned
- Generator expressions (`c for c in s.lower() if c.isalpha()`) are concise and memory-efficient for filtering.
- Sets are powerful for handling unique elements and performing operations like `issubset`.
- Breaking down a problem into steps (as in `is_pangram_long`) improves readability but may sacrifice brevity.
- Python's built-in methods like `isalpha()` simplify character validation.

## Files
- `is_pangram.py`: Contains the three solutions with detailed comments.