def cakes(recipe, available):
    """
    Berechnet die maximale Anzahl an Kuchen, die mit den verfügbaren Zutaten gebacken werden können.

    Args:
        recipe (dict): Dictionary mit Zutaten und deren benötigten Mengen pro Kuchen.
        available (dict): Dictionary mit verfügbaren Zutaten und deren Mengen.

    Returns:
        int: Maximale Anzahl an Kuchen, die gebacken werden können. Gibt 0 zurück,
             wenn eine benötigte Zutat fehlt.
    """
    max_cakes = float('inf')  # Initialisiere mit unendlich für Minimum-Berechnung

    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0  # Keine Kuchen möglich, wenn eine Zutat fehlt
        max_cakes = min(max_cakes, available[ingredient] // amount)  # Ganzzahlige Division

    return max_cakes if max_cakes != float('inf') else 0  # Handle leeres Rezept


def cakes_short(recipe, available):
    """
    Berechnet die maximale Anzahl an Kuchen, die mit den verfügbaren Zutaten gebacken werden können.

    Args:
        recipe (dict): Dictionary mit Zutaten und deren benötigten Mengen pro Kuchen.
        available (dict): Dictionary mit verfügbaren Zutaten und deren Mengen.

    Returns:
        int: Maximale Anzahl an Kuchen (Ganzzahl). Gibt 0 zurück, wenn eine Zutat fehlt.
    """
    return min(available.get(k, 0) // recipe[k] for k in recipe)  # Ganzzahlige Division pro Zutat


if __name__ == "__main__":
    # Testfälle
    test_cases = [
        (
            {"flour": 500, "sugar": 200, "eggs": 1},
            {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
            2,  # Erwartetes Ergebnis
            "Test 1: Standardfall mit genügend Zutaten"
        ),
        (
            {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000},
            0,  # Erwartetes Ergebnis
            "Test 2: Fehlende Zutat (apples)"
        ),
        (
            {},  # Leeres Rezept
            {"flour": 100, "sugar": 100},
            0,  # Erwartetes Ergebnis
            "Test 3: Leeres Rezept"
        )
    ]

    for recipe, available, expected, description in test_cases:
        result = cakes(recipe, available)
        print(f"{description}:")
        print(f"  Rezept: {recipe}")
        print(f"  Verfügbar: {available}")
        print(f"  Ergebnis: {result}, Erwartet: {expected}")
        print(f"  {'Erfolg' if result == expected else 'Fehler'}")
        print()