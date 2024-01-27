import re
import ssl
import tldextract

from socket import *
from typing import ByteString
from cachetools import cached, TTLCache

from whois.config import Settings


class Whois:
    def __init__(self, dname: str, whois_server: str=None) -> None:
        self.dname: str = dname
        self.whois_server: str = whois_server
    
    def _wrap_ssl(self) -> None:
        context: ssl.SSLContext = ssl.create_default_context()
        self.sock = context.wrap(self.sock, server_hostname=self.whois_server.split(':')[0])

    def _extract_whois_server(self, whois_data: str) -> str:
        whois_server_match = re.search(r'whois:\s+(.+)', whois_data, re.IGNORECASE)

        if whois_server_match:
            return whois_server_match.group(1)
        else:
            return None

    @cached(TTLCache(maxsize=Settings.CACHE_SIZE.value, ttl=Settings.CACHE_LIVETIME.value))
    def get_whois(self, whois_server: str, data: str) -> str:
        sock: int = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)

        sock.connect((whois_server, Settings.PORT.value))
        sock.send((data + '\r\n').encode())

        response: ByteString = b''

        while True:
            data = sock.recv(Settings.CHUNK_SIZE.value)
            if not data:
                break

            response += data
        
        sock.close()

        return response.decode()

    def request(self) -> None:
        if self.whois_server is None:
            tld = tldextract.extract(self.dname).suffix
            self.whois_server = self._extract_whois_server(
                self.get_whois(Settings.IANA_SERVER.value, tld)
            )

        if self.whois_server.endswith(f':{Settings.PORT.value}'):
            self._wrap_ssl()
        
        response = self.get_whois(self.whois_server, self.dname).lstrip()

        return response
