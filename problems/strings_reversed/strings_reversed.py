# Solution for Codewars: Spin Words
# Problem: https://www.codewars.com/kata/5264d2b162488dc400000001
#
# Description: Write a function that takes a string of one or more words and returns
# the same string with all words of five or more letters reversed. The string consists
# only of letters and spaces, with spaces included only when multiple words are present.
#
# Approach:
# - Use `split()` to split the input string into a list of words, using whitespace as the delimiter.
# - Iterate through each word, reversing it with slicing (`[::-1]`) if it has 5 or more letters.
# - Collect processed words in a list.
# - Use `join()` to combine the words back into a string with spaces as separators.
#
# Notes:
# - `split()`: A C-implemented method that splits a string into a list, treating consecutive
#   whitespace as a single delimiter.
# - Slicing `[::-1]`: Reverses a string by starting from the last character (default start),
#   ending at the first (default stop), with a step of -1 (backwards).
# - `join()`: A C-implemented method that concatenates a list of strings, inserting the
#   specified delimiter (here, a space) between elements.

def spin_words(sentence: str) -> str:
    """Reverses words with 5 or more letters in a given string.

    Args:
        sentence (str): Input string containing words separated by spaces.

    Returns:
        str: String with words of 5+ letters reversed, others unchanged.
    """
    # Split the sentence into a list of words
    words = sentence.split()
    # Initialize a list for processed words
    result = []

    # Process each word
    for word in words:
        if len(word) >= 5:
            # Reverse words with 5 or more letters
            result.append(word[::-1])
        else:
            # Keep shorter words unchanged
            result.append(word)

    # Join words with a space and return the result
    return " ".join(result)

#List Comprehension
#(expression for item in iterable)
#ternäre Operation (x if condition else y)
#[] List

def spin_words_list(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#Generator Expression
#(expression for item in iterable)
#ternäre Operation (x if condition else y)
#() Generator
def spin_words_generator(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

# Example usage
if __name__ == "__main__":
    test_cases = [
        "Hey fellow warriors",
        "This is a test",
        "This is another test",
        "Welcome",
        ""
    ]
    for test in test_cases:
        print(f"Input: '{test}' -> Output: '{spin_words(test)}'")