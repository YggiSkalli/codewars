# Tribonacci Sequence - Codewars Problem

## Problem Description
- **Link**: [Tribonacci Sequence on Codewars](https://www.codewars.com/kata/556deca17c58da83c00002db)
- **Task**: Generate the first `n` elements of a Tribonacci sequence given a starting `signature` (typically 3 elements). The Tribonacci sequence sums the last three numbers to generate the next, e.g., with `signature = [1, 1, 1]`, the sequence is `[1, 1, 1, 3, 5, 9, 17, 31, ...]`.
- **Requirements**:
  - Handle `n == 0` (return `[]`).
  - Handle `n <= len(signature)` (return first `n` elements).
  - Handle `n > len(signature)` (extend the sequence).

## Solutions

### 1. Iterative Solution (Recommended)
- **File**: `tribonacci_sequence.py`
- **Approach**: Initialize result with `signature[:n]`, then append new elements using a `for` loop with `sum(res[-3:])`.
- **Why Preferred?**: Efficient (no recursion overhead), robust for all edge cases, readable.
- **Code**:
  ```python
  def tribonacci(signature: list, n: int) -> list:
      res = signature[:n]
      for i in range(max(0, n - len(signature))):
          res.append(sum(res[-3:]))
      return res