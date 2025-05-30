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
    "a" * 139                                =>  "#A" + "a" * 138 (140 chars, valid)
    "a" * 140                                =>  False (141 chars with #, invalid)
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

import time
import random
import string

def generate_hashtag(s):
    result = "#" + "".join(word.capitalize() for word in s.split())
    return result if 1 < len(result) < 141 else False


def generate_hashtag_alternative(s):
    result = "#" + s.title().replace(' ', '')
    return result if 1 < len(result) < 141 else False


def generate_test_input(length, num_words):
    """Generate a random string with specified length and number of words."""
    # Begrenze num_words auf die maximale Anzahl möglicher Wörter
    num_words = min(num_words, length)  # Ein Wort braucht mindestens 1 Zeichen
    if num_words == 0 or length == 0:
        return ""

    words = []
    remaining_length = length
    for _ in range(num_words - 1):
        # Mindestens 1 Zeichen pro Wort, maximal remaining_length // verbleibende Wörter
        word_length = random.randint(1, max(1, remaining_length // (num_words - len(words))))
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
        remaining_length -= word_length

    # Letztes Wort nimmt restliche Länge
    if remaining_length > 0:
        words.append(''.join(random.choices(string.ascii_lowercase, k=remaining_length)))

    return ' '.join(words)


def performance_test():
    # Generate test inputs
    test_inputs = [
        generate_test_input(random.randint(10, 130), random.randint(1, 20)) for _ in range(1000)
    ]
    test_inputs.extend(["", " ", "a" * 139, "a" * 140, "hello world"])

    # Test generate_hashtag
    start_time = time.perf_counter()
    for s in test_inputs:
        generate_hashtag(s)
    elapsed_time = time.perf_counter() - start_time
    print(f"generate_hashtag took {elapsed_time:.6f} seconds for {len(test_inputs)} inputs")

    # Test generate_hashtag_alternative
    start_time = time.perf_counter()
    for s in test_inputs:
        generate_hashtag_alternative(s)
    elapsed_time = time.perf_counter() - start_time
    print(f"generate_hashtag_alternative took {elapsed_time:.6f} seconds for {len(test_inputs)} inputs")


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

    # Run functional tests
    print("Testing generate_hashtag:")
    for test_input, expected in test_cases:
        output = generate_hashtag(test_input)
        print(f"Input: '{test_input}' -> Output: {output}, Expected: {expected}, {'Pass' if output == expected else 'Fail'}")

    print("\nTesting generate_hashtag_alternative:")
    for test_input, expected in test_cases:
        output = generate_hashtag_alternative(test_input)
        print(f"Input: '{test_input}' -> Output: {output}, Expected: {expected}, {'Pass' if output == expected else 'Fail'}")

    # Run performance test
    print("\nRunning performance test...")
    performance_test()