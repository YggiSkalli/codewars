"""
Hashtag Generator

This script solves the Codewars problem "Hashtag Generator".
https://www.codewars.com/kata/52449b062fb80683ec000024

The task is to convert a string into a hashtag with the following rules:
    - It must start with a hashtag (#).
    - All words must have their first letter capitalized and the rest lowercase.
    - If the final result (including #) is longer than 140 characters, return False.
    - If the input or the result is an empty string, return False.

Examples:
    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""                                        =>  False
    "a" * 140                                =>  False (since # + 140 chars = 141 > 140)

The solution processes the string as follows:
    1. Split the input string into words, removing extra whitespace.
    2. Capitalize each non-empty word and join them into a single string.
    3. Prepend a hashtag (#) if the result is non-empty and less than 140 characters.
    4. Return False for empty inputs/results or if the final length exceeds 140.

Time Complexity: O(n), where n is the length of the input string.
    - Splitting the string: O(n)
    - Capitalizing words and joining: O(n)
    - Length checks and string concatenation: O(n)

Space Complexity: O(n)
    - Storing the list of words and the result string: O(n)
"""

def generate_hashtag(s):
    result = "".join(word.capitalize() for word in s.split() if word)
    return "#" + result if result and len(result) < 140 else False


def generate_hashtag_alternative(s):
    result = "#" + s.title().replace(' ', '')
    return result if 1 < len(result) < 141 else False


if __name__ == "__main__":
    """
    Test the solution with various strings.
    This block runs when the script is executed directly, allowing us to verify the function's behavior.
    """
    # List of test cases with expected outputs
    test_cases = [
        (" Hello there thanks for trying my Kata", "#HelloThereThanksForTryingMyKata"),
        ("    Hello     World   ", "#HelloWorld"),
        ("", False),
        (" ", False),
        ("a" * 139, "#A" + "a" * 138),  # 139 chars + # = 140, valid
        ("a" * 140, False),           # 140 chars + # = 141, invalid
        ("hello world", "#HelloWorld"),
        ("   ", False),
        ("code" + " " * 5 + "wars", "#CodeWars"),
    ]

    # Iterate over each test case and print the input, output, and expected output for both functions
    print("Testing generate_hashtag:")
    for test_input, expected in test_cases:
        output = generate_hashtag(test_input)
        print(f"Input: '{test_input}' -> Output: {output}, Expected: {expected}, {'Pass' if output == expected else 'Fail'}")

    print("\nTesting generate_hashtag_alternative:")
    for test_input, expected in test_cases:
        output = generate_hashtag_alternative(test_input)
        print(f"Input: '{test_input}' -> Output: {output}, Expected: {expected}, {'Pass' if output == expected else 'Fail'}")


