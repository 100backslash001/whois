# Whois Lookup
### The web version of the whois client that is based on
- [flask](https://pypi.org/project/Flask/) ( backend )
- [js/css/html](https://www.w3.org) ( frontend )
- [socket](https://docs.python.org/3/library/socket.html) ( for whois queries )
- [ssl](https://docs.python.org/3/library/ssl.html#module-ssl) ( wraps socket )
- [tldextract](https://pypi.org/project/tldextract/) ( extracts tld from dname )
- [cachetools](https://pypi.org/project/cachetools/) ( caches requests )

## How does it work

When a domain name is requested, it is passed to the `whois.query.Whois( 'example.com' ).request()` module, the module extracts a tld from the domain name via `tldextract` to query `whois.iana.org` to find the whois server responsible for the domain zone. The query then goes to the responsible server to get information about the domain name. Connection to the servers is on port 43 https://datatracker.ietf.org/doc/html/rfc3912#section-2.