# Multiples of 3 or 5

## Problem Description
[Link to Codewars](https://www.codewars.com/kata/514b92a6575fc95c0b000006)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the number passed in. If the number is negative, return 0. If a number is a multiple of both 3 and 5, only count it once.

## Solutions

### 1. Mathematical Formula
- **Approach**: Uses the arithmetic series formula with inclusion-exclusion to calculate the sum in O(1) time.
- **Pros**: Highly efficient, works well for large inputs.
- **Cons**: Less intuitive, requires mathematical understanding.
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

### 2. List Comprehension
- **Approach**: Iterates through numbers below the input and sums those divisible by 3 or 5.
- **Pros**: Simple, readable, pythonic.
- **Cons**: Slower for large inputs due to O(n) time complexity.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (generator expression avoids storing the list)

## Example
```python
solution_formula(10)  # Returns 23 (3 + 5 + 6 + 9)
solution_loop(10)     # Returns 23

