def rgb(r, g, b):
    hex_digits = "0123456789ABCDEF"

    def to_hex(value):
        # Begrenze Wert auf 0 bis 255
        value = max(0, min(255, value))
        # Konvertiere zu Hex, entferne "0x" und füge führende Null hinzu
        return hex_digits[value // 16] + hex_digits[value % 16]

    return to_hex(r) + to_hex(g) + to_hex(b)


def rgb_string_convert(r, g, b):
    def to_hex(value):
        # Begrenze Wert auf 0 bis 255
        value = max(0, min(255, value))
        # Konvertiere zu Hex, entferne "0x" und füge führende Null hinzu
        return f"{value:02X}"

    return to_hex(r) + to_hex(g) + to_hex(b)

if __name__ == "__main__":
    """
    Test the solution with various RGB values.
    This block runs when the script is executed directly, allowing us to verify the function's behavior.
    """
    # List of test cases with expected outputs
    test_cases = [
        ((255, 255, 255), "FFFFFF"),  # Maximalwerte
        ((255, 255, 300), "FFFFFF"),  # Wert > 255, muss auf 255 gerundet werden
        ((0, 0, 0), "000000"),       # Minimalwerte
        ((148, 0, 211), "9400D3"),   # Gemischte Werte
        ((-20, 0, 255), "0000FF"),   # Negativer Wert, muss auf 0 gerundet werden
        ((1, 2, 3), "010203"),       # Kleine Werte mit führenden Nullen
        ((254, 253, 252), "FEFCFC"), # Werte knapp unter 255
    ]

    # Iterate over each test case and print the input and output
    for (r, g, b), expected in test_cases:
        result = rgb(r, g, b)
        result_string_convert = rgb_string_convert(r, g, b)
        print(f"Test: rgb({r}, {g}, {b}) -> Expected: {expected}, Got: {result}, String Convert: {result_string_convert}, Pass: {result == expected and result_string_convert == expected}")
