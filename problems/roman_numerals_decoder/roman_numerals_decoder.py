"""
Roman Numerals Decoder

This script solves the Codewars problem "Roman Numerals Decoder".
The task is to convert a Roman numeral string into its decimal (integer) representation.
Roman numerals use the following symbols: I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
The value is calculated by adding the symbols from left to right, but if a smaller symbol precedes a larger one, it is subtracted (e.g., IV = 5 - 1 = 4).

Example:
- "III" -> 3 (1 + 1 + 1)
- "IV" -> 4 (5 - 1)
- "IX" -> 9 (10 - 1)
- "LVIII" -> 58 (50 + 5 + 1 + 1 + 1)
- "MCMXCIV" -> 1994 (1000 + (1000 - 100) + (100 - 10) + (5 - 1))

The solution processes the string from right to left, comparing each symbol's value with the previous one:
- If the current value is >= the previous value, add it.
- If the current value is < the previous value, subtract it.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(1), as we use a fixed-size dictionary and a few variables.
"""

def solution(roman: str) -> int:
    """
    Convert a Roman numeral string to its decimal value.

    Args:
        roman (str): A string containing a valid Roman numeral (e.g., "MCMXCIV").

    Returns:
        int: The decimal value of the Roman numeral (e.g., 1994 for "MCMXCIV").
    """
    # Dictionary mapping Roman numeral symbols to their decimal values
    # I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize variables:
    # prev_value keeps track of the last processed symbol's value for comparison
    # result accumulates the final decimal value
    prev_value = 0
    result = 0

    # Process the string from right to left using reversed()
    # This simplifies the subtraction rule: if a smaller value comes before a larger one in the original string,
    # it will be processed after the larger one when going right-to-left, allowing us to subtract it
    # Example: In "IV" (4), we process V (5) first, then I (1), and subtract I because 1 < 5
    for number in reversed(roman):
        # Get the decimal value of the current Roman symbol
        current_value = roman_values[number]

        # If the current value is greater than or equal to the previous value,
        # add it to the result
        # Example: In "III" (3), we process I (1), I (1), I (1) from right to left
        # Each I is >= the previous value (0, then 1, then 1), so we add: 1 + 1 + 1 = 3
        if current_value >= prev_value:
            result += current_value
        # If the current value is less than the previous value, subtract it
        # Example: In "IV" (4), we process V (5), then I (1)
        # I (1) < V (5), so we subtract: 5 - 1 = 4
        else:
            result -= current_value

        # Update prev_value to the current value for the next iteration
        prev_value = current_value

    # Return the final decimal value
    return result


if __name__ == "__main__":
    """
    Test the solution with various Roman numerals.
    This block runs when the script is executed directly, allowing us to verify the function's behavior.
    """
    # List of test cases with expected outputs
    test_cases = [
        "III",    # Expected: 3
        "IV",     # Expected: 4
        "IX",     # Expected: 9
        "LVIII",  # Expected: 58
        "MCMXCIV" # Expected: 1994
    ]

    # Iterate over each test case and print the input and output
    for test in test_cases:
        print(f"{test} -> {solution(test)}")