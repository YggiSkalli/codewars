# Roman Numerals Decoder

## Problem Description

The task is to create a function that converts a Roman numeral string into its decimal (integer) representation. Roman numerals are based on specific symbols: `I` (1), `V` (5), `X` (10), `L` (50), `C` (100), `D` (500), and `M` (1000). The value of a Roman numeral is calculated by adding the symbols from left to right, but if a smaller symbol precedes a larger one, it is subtracted (e.g., `IV` = 5 - 1 = 4).

### Examples
- `"III"` → `3` (1 + 1 + 1)
- `"IV"` → `4` (5 - 1)
- `"IX"` → `9` (10 - 1)
- `"LVIII"` → `58` (50 + 5 + 1 + 1 + 1)
- `"MCMXCIV"` → `1994` (1000 + (1000 - 100) + (100 - 10) + (5 - 1))

### Constraints
- The input string contains only valid Roman numeral symbols (`I`, `V`, `X`, `L`, `C`, `D`, `M`).
- The input is guaranteed to be a valid Roman numeral in the range [1, 3999].

## Solution

### Approach
The solution processes the Roman numeral string from right to left (using `reversed()`). It uses a dictionary to map Roman symbols to their decimal values. For each symbol:
- If the current value is greater than or equal to the previous value, add it to the result.
- If the current value is less than the previous value, subtract it (this handles cases like `IV`, where `I` is subtracted from `V`).

This approach works because, in a valid Roman numeral, a smaller value before a larger one always indicates subtraction, and processing from right to left simplifies the logic.

### Time Complexity
- **Time Complexity**: O(n), where n is the length of the input string. We iterate through the string exactly once.
- **Space Complexity**: O(1), as we only use a fixed-size dictionary and a few variables, regardless of input size.

### Files
- `roman_numerals_decoder.py`: The solution with detailed comments.

## Example Walkthrough
For input `"MCMXCIV"`:
1. Start with `result = 0`, `prev_value = 0`.
2. Process from right to left (`reversed("MCMXCIV")` → `V, I, C, X, M, C, M`):
   - `V` (5): `5 >= 0`, `result = 5`, `prev_value = 5`
   - `I` (1): `1 < 5`, `result = 5 - 1 = 4`, `prev_value = 1`
   - `C` (100): `100 > 1`, `result = 4 + 100 = 104`, `prev_value = 100`
   - `X` (10): `10 < 100`, `result = 104 - 10 = 94`, `prev_value = 10`
   - `M` (1000): `1000 > 10`, `result = 94 + 1000 = 1094`, `prev_value = 1000`
   - `C` (100): `100 < 1000`, `result = 1094 - 100 = 994`, `prev_value = 100`
   - `M` (1000): `1000 > 100`, `result = 994 + 1000 = 1994`, `prev_value = 1000`
3. Return `1994`.

## Test Cases
- `"III"` → `3`
- `"IV"` → `4`
- `"IX"` → `9`
- `"LVIII"` → `58`
- `"MCMXCIV"` → `1994`

## Alternative Approaches
1. **Counting with Correction**: Count occurrences of each symbol and subtract for combinations like `IV`, `IX`, etc. (see the intelligent solution with `values`).
2. **Precomputed Lookup**: Use a compressed list of all Roman numerals from 1 to 3999 and find the index (see the creative solution with Base64 and LZMA).

## Lessons Learned
- Processing Roman numerals from right to left simplifies the subtraction rule.
- Understanding the structure of Roman numerals (e.g., `IV` = 4, not 6) is key to solving this problem efficiently.
- Dictionaries are a great way to map symbols to values in Python.