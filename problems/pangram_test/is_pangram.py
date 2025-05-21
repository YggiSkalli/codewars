# Problem: Check if a string is a pangram (contains every letter of the alphabet at least once).
# Ignore case, numbers, and punctuation.
# Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python


def is_pangram(st):
    """
    Concise solution to check if a string is a pangram.
    Uses a generator expression to filter letters and a set to count unique ones.

    Args:
        st (str): Input string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    # Convert to lowercase and create a set of unique alphabetic characters
    # Check if the length is 26 (number of letters in the alphabet)
    return len(set(c for c in st.lower() if c.isalpha())) == 26


def is_pangram_long(st):
    """
    Verbose solution to check if a string is a pangram.
    Breaks down the process into clear steps for readability.

    Args:
        st (str): Input string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    # Step 1: Convert string to lowercase for case-insensitive check
    st_lower = st.lower()

    # Step 2: Collect alphabetic characters in a list
    letters = [c for c in st_lower if c.isalpha()]

    # Step 3: Convert to set to remove duplicates
    unique_letters = set(letters)

    # Step 4: Check if there are 26 unique letters
    return len(unique_letters) == 26


def is_pangram_subset(s):
    """
    Alternative solution using subset check.
    Compares the alphabet against the string's letters.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    # Check if the full alphabet is a subset of the string's alphabetic characters
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(c for c in s.lower() if c.isalpha()))