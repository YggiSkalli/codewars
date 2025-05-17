# Extract the Domain Name from a URL

## Description
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

### Examples
- `"http://github.com/carbonfive/raygun"` -> `"github"`
- `"http://www.zombie-bites.com"` -> `"zombie-bites"`
- `"https://www.cnet.com"` -> `"cnet"`

### Task
- The function should handle URLs with or without protocols (`http://`, `https://`), with or without `www`, and with or without paths (e.g., `/path`).
- The domain name is the part between `www` (if present) and the top-level domain (e.g., `.com`).

## Solution
The solution is implemented in `extract_the_domain_name.py`. It uses string splitting to:
1. Remove the protocol by splitting at `//` and taking the last part.
2. Remove the path by splitting at `/` and taking the first part.
3. Split the domain at `.` to handle subdomains (`www`) and extract the domain name.

## Example Usage
```python
from extract_the_domain_name import domain_name

print(domain_name("http://github.com/carbonfive/raygun"))  # Output: github
print(domain_name("http://www.zombie-bites.com"))         # Output: zombie-bites
print(domain_name("https://www.cnet.com"))                # Output: cnet