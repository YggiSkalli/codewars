def divide_and_multiply(n):
    """
    Computes the sum of modified numbers from array n after optimally dividing by 2 and multiplying.
    Each number in n can be divided by 2 as many times as possible, collecting division operations.
    Then, one number can be multiplied by 2 for each collected division.
    Returns the maximum possible sum modulo 10^9 + 7.

    Args:
        n (list): List of positive integers.

    Returns:
        int: Maximum possible sum after operations, modulo 10^9 + 7.
    """
    MOD = 1_000_000_007  # Modulo constant for result.

    ops = 0  # Tracks total number of division-by-2 operations. !0 weil +1 +1 +1
    odd_values = []  # Stores numbers after dividing out all factors of 2.
    for num in n:
        while num % 2 == 0:  # Divide by 2 as long as possible.
            ops += 1  # Increment operation counter.
            num //= 2  # Perform division.
        odd_values.append(num)  # Store the odd number after divisions.

    # Calculate sum of odd values plus max odd value times (2^ops - 1).
    # Using pow() for efficient modular exponentiation could be considered.
    return (sum(odd_values) + max(odd_values) * (2 ** ops - 1)) % MOD


def divide_and_multiply_bitshift(n):
    """
    Alternative solution using bit-shift operations for efficiency.
    Computes the same result as divide_and_multiply but optimizes division by
    using bitwise operations to extract powers of 2.

    Args:
        n (list): List of positive integers.

    Returns:
        int: Maximum possible sum after operations, modulo 10^9 + 7.
    """
    MOD = 1_000_000_007  # Modulo constant for result.
    total_power = 1  # Accumulates total power of 2 from all numbers. !1  weil *2 *2 *2
    odd_values = []  # Stores numbers after dividing out all factors of 2.

    for x in n:
        # Find the largest power of 2 dividing x using bitwise AND with -x.
        # x & -x gives the lowest set bit (e.g., 24 -> 8).
        lowest_bit = x & -x
        odd_values.append(x // lowest_bit)  # Store number after removing power of 2.
        total_power *= lowest_bit  # Accumulate the power of 2.

    # Same formula: sum of odd values + max odd value * (total_power - 1).
    return (sum(odd_values) + max(odd_values) * (total_power - 1)) % MOD


# Tests
if __name__ == "__main__":
    print(divide_and_multiply([30, 64]))  # Expected: 1921
    print(divide_and_multiply([4, 2, 3]))  # Expected: 26
    print(divide_and_multiply_bitshift([30, 64]))  # Expected: 1921
    print(divide_and_multiply_bitshift([4, 2, 3]))  # Expected: 26(korrekt)