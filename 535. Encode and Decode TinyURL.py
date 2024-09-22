class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        code = str(self.counter)
        self.counter += 1

        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl

        return self.base_url + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))