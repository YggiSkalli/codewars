#Die Syntax c for c in s.lower() if c.isalpha() ist ein Generator-Ausdruck


def is_pangram(st):
    return len(set(c for c in st.lower() if c.isalpha()))  == 26


def is_pangram_long(st):
    # Schritt 1: String in Kleinbuchstaben umwandeln
    st_lower = st.lower()

    # Schritt 2: Liste von alphabetischen Zeichen erstellen
    letters = []
    for c in st_lower:
        if c.isalpha():
            letters.append(c)

    # Schritt 3: In ein Set umwandeln, um Duplikate zu entfernen
    unique_letters = set(letters)

    # Schritt 4: Prüfen, ob 26 verschiedene Buchstaben vorhanden sind
    return len(unique_letters) == 26