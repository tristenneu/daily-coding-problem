'''
Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
'''

# SOLUTION

import hashlib


class UrlShortener:

    def __init__(self):
        self.short_to_url_map = dict()
        self.m = hashlib.sha256
        self.prefix = 'http://urlsho.rt/'

    def shorten(self, url):
        sha_signature = self.m(url.encode()).hexdigest()
        short_hash = sha_signature[:6]
        self.short_to_url_map[short_hash] = url
        return self.prefix + short_hash

    def restore(self, short):
        short_hash = short.replace(self.prefix, '')
        return self.short_to_url_map[short_hash]


url_0 = 'https://www.tutorialspoint.com/python/string_replace.htm'
us = UrlShortener()
short_0 = us.shorten(url_0)
print(us.restore(short_0)) # url_0
short_1 = us.shorten(url_0)
print(us.restore(short_1)) # url_0