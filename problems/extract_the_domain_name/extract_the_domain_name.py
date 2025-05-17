# Solution for Codewars: Extract the Domain Name from a URL
# Problem: https://www.codewars.com/kata/514a024011ea4fb54200004b
#
# Description: Write a function that extracts the domain name from a URL string and returns it as a string.
# Examples:
# - "http://github.com/carbonfive/raygun" -> "github"
# - "http://www.zombie-bites.com" -> "zombie-bites"
# - "https://www.cnet.com" -> "cnet"
# The function must handle URLs with or without protocol (http://, https://), with or without www,
# and with or without paths (e.g., /path). The domain name is the part between www (if present) and
# the top-level domain (e.g., .com).
#
# Approach:
# - Split the URL at '//' to remove the protocol (http:// or https://).
# - Split at '/' to remove the path, keeping only the domain part.
# - Split the domain at '.' to separate subdomains (e.g., www), the domain name, and top-level domains.
# - Check if the first part is 'www'; if so, return the second part; otherwise, return the first part.
#
# Notes:
# - url.split('//')[-1]: Robustly handles URLs with or without protocol (e.g., "github.com" works).
#   Time complexity is O(n) where n is the length of the URL string.
# - start.split('/')[0]: Safely extracts the domain even if no path exists (e.g., "github.com").
#   Handles edge cases like trailing slashes (e.g., "github.com/").
# - domain.split('.'): Splits into parts, assuming at least one dot exists in valid domains.
#   For edge cases like "localhost" (no dots), the solution may need adjustment, but Codewars tests
#   assume standard domains (e.g., .com, .org).
# - Conditional check for 'www': Simple and effective for the given test cases, but may not handle
#   complex subdomains (e.g., sub.sub.domain.com), which are not required by the problem.
# - Memory complexity: O(n) due to string splitting creating new lists of substrings.
# - The solution assumes valid URLs with at least one dot in the domain part and does not validate
#   malformed inputs (e.g., empty strings, missing domains), as not required by the problem.

def domain_name(url: str) -> str:
    """Extracts the domain name from a URL string.

    Args:
        url (str): The input URL (e.g., "http://github.com/carbonfive/raygun").

    Returns:
        str: The domain name (e.g., "github").
    """
    # Teile die URL bei '//' und nimm den letzten Teil, um das Protokoll (http:// oder https://) zu entfernen
    start = url.split('//')[-1]

    # Teile bei '/' und nimm den ersten Teil, um den Pfad (alles nach der Domain) zu entfernen
    domain = start.split('/')[0]

    # Teile die Domain bei Punkten, um Subdomains und Top-Level-Domains zu trennen
    parts = domain.split('.')

    # Prüfe, ob der erste Teil 'www' ist; wenn ja, nimm den zweiten Teil als Domainnamen
    if parts[0] == 'www':
        return parts[1]

    # Wenn kein 'www' vorhanden ist, nimm den ersten Teil als Domainnamen
    return parts[0]

# Example usage
if __name__ == "__main__":
    # Liste von Test-URLs, die die Funktion manuell überprüfen
    test_cases = [
        ("http://github.com/carbonfive/raygun"),
        ("http://www.zombie-bites.com"),
        ("https://www.cnet.com")
    ]
    # Iteriere über die Testfälle und gib Eingabe und Ausgabe der Funktion aus
    for domain in test_cases:
        print(f"Input: url={domain} -> Output: {domain_name(domain)}")