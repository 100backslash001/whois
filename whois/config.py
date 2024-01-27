from enum import Enum


class Settings(Enum):
    PORT = 43
    IANA_SERVER = 'whois.iana.org'
    CHUNK_SIZE = 4096
    CACHE_SIZE = 100
    CACHE_LIVETIME = 3600