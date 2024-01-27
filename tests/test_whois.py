import unittest
from unittest.mock import patch, MagicMock

import ssl

import whois.query as whois


class TestWhois(unittest.TestCase):
    def test_no_domain_was_passed(self):
        with self.assertRaises(TypeError):
            whois.Whois()

    def test_cannot_get_whois_server(self):
        with self.assertRaises(AttributeError):
            whois_test = whois.Whois('domainTEST')

            whois_test.request()
    
    @patch('whois.query.Whois._wrap_ssl')
    def test_could_not_create_ssl_context(self, _wrap_ssl):
        _wrap_ssl.side_effect = ssl.SSLError('Error Occured')

        with self.assertRaises(ssl.SSLError):
            whois_test = whois.Whois('test.com')
            whois_test._wrap_ssl()


if __name__ == '__main__':
    unittest.main()