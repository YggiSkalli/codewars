# Strings Reversed 

## Problem Description
[Link to Codewars](https://www.codewars.com/kata/5264d2b162488dc400000001/python)
 
Write a function that takes a string of one or more words and returns the same string, but with all words that have five or more letters reversed. Strings consist of only letters and spaces. Spaces are included only when more than one word is present.

## Solutions

## Solutions

### 1. Use of split(), join(), and slicing [start:stop:step]
- **Approach**:
  - The input string is split into a list of words using `split()`, with spaces as delimiters.
  - For each word, its length is checked: if it has 5 or more letters, it is reversed using slicing (`[::-1]`); otherwise, it remains unchanged.
  - The processed words are collected in a new list.
  - The list is joined back into a single string using `join()` with a space as the separator.
- **Pros**:
  - Simple and readable: The code is concise, clear, and uses standard Python methods, making it easy to understand.
  - Efficient: `split()`, `join()`, and slicing are implemented in C, ensuring fast execution.
  - Flexible: Works for any input with letters and spaces, as specified.
  - No external libraries: Uses only built-in Python functions, ensuring portability.
- **Cons**:
  - Memory usage: Creates a new list and new strings, which may use more memory for very long inputs.
  - Limited adaptability: The solution is specific to reversing words with 5+ letters and not easily modified for other criteria.
  - Relies on Python internals: Depends on optimized C implementations, which may be slower in non-CPython interpreters (e.g., PyPy).
- **Time Complexity**: O(n), where n is the total length of the input string.
  - `split()`: O(n) to traverse the string.
  - Word processing loop: O(n), as each character is processed once.
  - Slicing (`[::-1]`): O(k) for a word of length k, summing to O(n) across all words.
  - `join()`: O(n) to copy all characters.
- **Space Complexity**: O(n), where n is the total length of the input string.
  - `split()`: O(n) for the list of words.
  - Result list: O(n) for processed words.
  - `join()`: O(n) for the final string.

### 2. Manual word reversal with character swapping
- **Approach**:
  - Split the input string into words using `split()`.
  - For each word with 5+ letters, convert it to a list of characters, swap characters from both ends inward, and join them back to a string.
  - Collect processed words in a list and join them with `join()`.
- **Pros**:
  - Explicit control over reversal process, similar to low-level programming.
  - Educational for understanding string manipulation.
- **Cons**:
  - More complex and less readable than slicing.
  - Slower due to manual character swapping in Python.
- **Time Complexity**: O(n), but with higher constants due to manual swapping.
- **Space Complexity**: O(n), similar to the slicing approach.
- 
## Example
```python
spin_words("Hey fellow warriors")  # Returns "Hey wollef sroirraw"
spin_words("This is a test")      # Returns "This is a test"
spin_words("This is another test") # Returns "This is rehtona test"
