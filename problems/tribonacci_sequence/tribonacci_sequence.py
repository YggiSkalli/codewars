# Solution for Codewars: Tribonacci Sequence
# Problem: https://www.codewars.com/kata/556deca17c58da83c00002db
#
# Description: Write a function that generates the first n elements of a Tribonacci sequence
# given a starting signature (a list of numbers, typically 3 elements). The Tribonacci sequence
# sums the last three numbers to generate the next, e.g., with signature [1, 1, 1], the sequence
# is [1, 1, 1, 3, 5, 9, 17, 31, ...]. The function must handle n == 0 (return []), n <= len(signature)
# (return first n elements), and n > len(signature) (extend the sequence).
#
# Approach:
# - Use recursion with a base case: if n <= len(signature), return signature[:n].
# - For n > len(signature), recursively call the function with a new signature that appends
#   the sum of the last three elements (sum(signature[-3:])).
# - The recursion builds the sequence by extending the signature until it is long enough.
#
# Notes:
# - List slicing (signature[:n]): Returns the first n elements, handling n == 0 (returns []) and
#   n <= len(signature). Time complexity is O(n).
# - sum(signature[-3:]): Sums the last three elements using negative indexing, concise and robust
#   for signatures with at least 3 elements. Slicing creates a new list (O(1) for small slices),
#   and sum() is O(k) where k is the slice length (here, 3).
# - List concatenation (signature + [sum(...)]): Creates a new list each recursive call, with
#   O(k) complexity where k is the signature length, leading to O(n * k) total overhead for
#   n - len(signature) calls.
# - Recursion depth: The function makes n - len(signature) recursive calls, risking a RecursionError
#   for large n (Python's default limit is 1000). Iterative solutions are more efficient.
# - The solution assumes signature has at least 3 elements, but sum(signature[-3:]) handles
#   shorter signatures by summing available elements, which may not align with Tribonacci rules.
#

def tribonacci(signature: list, n: int) -> list:
    """Generates the first n elements of a Tribonacci sequence from a given signature.

    Args:
        signature (list): Starting list of numbers (typically 3 elements, e.g., [1, 1, 1]).
        n (int): Number of elements to return in the sequence.

    Returns:
        list: List containing the first n elements of the Tribonacci sequence.
    """
    # Base case: return first n elements if n <= len(signature)
    # Recursive case: extend signature with sum of last 3 elements and recurse
    return (signature[:n] if n <= len(signature) else
            tribonacci(signature + [sum(signature[-3:])], n))


# Alternative Implementation: Recursive with Memoization
# Approach: Use memoization to cache intermediate sequences, reducing redundant list creations.
# This is less practical for Codewars due to overhead but included for completeness.
#
from functools import lru_cache

@lru_cache(maxsize=None)
def tribonacci_memoized(signature: tuple, n: int) -> list:
    """Alternative recursive implementation with memoization."""
    # Convert tuple back to list for slicing
    signature = list(signature)
    # Base case: return first n elements if n <= len(signature)
    # Recursive case: extend signature with sum of last 3 elements and recurse
    return (signature[:n] if n <= len(signature) else
            tribonacci_memoized(tuple(signature + [sum(signature[-3:])]), n))


# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 8),  # Expected: [1, 1, 1, 3, 5, 9, 17, 31]
        ([1, 1, 1], 1),  # Expected: [1]
        ([1, 1, 1], 0),  # Expected: []
        ([1, 2, 3, 4], 6),  # Expected: [1, 2, 3, 4, 9, 16]
        ([1, 1], 5),  # Edge case: signature with < 3 elements
    ]
    for signature, n in test_cases:
        print(f"Input: signature={signature}, n={n} -> Output: {tribonacci(signature, n)}")