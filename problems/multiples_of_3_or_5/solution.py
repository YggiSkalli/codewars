# Solution for Codewars: Multiples of 3 or 5
# Problem: https://www.codewars.com/kata/514b92a6575fc95c0b000006

# Approach 1: Mathematical Formula (O(1) time complexity)
def solution_formula(number):
    """Calculate the sum of multiples of 3 or 5 below number using inclusion-exclusion."""
    if number <= 0:
        return 0
    def sum_multiples(d, n):
        count = (n - 1) // d
        return d * (count * (count + 1)) // 2
    return sum_multiples(3, number) + sum_multiples(5, number) - sum_multiples(15, number)

# Approach 2: List Comprehension (O(n) time complexity)
def solution_loop(number):
    """Calculate the sum of multiples of 3 or 5 below number using a loop."""
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# Example usage
if __name__ == "__main__":
    print(solution_formula(10))  # Output: 23
    print(solution_loop(10))     # Output: 23