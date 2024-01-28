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
    
    def test_get_whois_raise_if_server_or_domain_not_passed(self):
        whois_test = whois.Whois('test.com')
        
        with self.assertRaises(TypeError):
            whois_test.get_whois()

    def test_request_return_data(self):
        whois_test = whois.Whois('google.com')
        expected_result = r'Domain Name: GOOGLE.COM'
        
        actual_result = whois_test.request()

        self.assertIsInstance(actual_result, str)

        self.assertRegex(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()