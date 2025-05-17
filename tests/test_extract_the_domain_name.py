import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'problems', 'extract_the_domain_name')))

import unittest
from extract_the_domain_name import domain_name

class TestDomainName(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(domain_name("http://github.com/carbonfive/raygun"), "github")
        self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")
        self.assertEqual(domain_name("https://www.cnet.com"), "cnet")

    def test_no_protocol(self):
        self.assertEqual(domain_name("github.com"), "github")

    def test_trailing_slash(self):
        self.assertEqual(domain_name("http://github.com/"), "github")

if __name__ == "__main__":
    unittest.main()