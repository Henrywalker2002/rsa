from Math import Math


class Private_key:

    def __init__(self, d: int, n: int):
        self.d = d
        self.n = n


class Public_key:

    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n


class RSA:

    def __init__(self):
        p, q = Math.find_p_and_q()
        n = p*q
        m = (p-1)*(q-1)
        e = Math.find_e(m)
        d = Math.find_d(e, m)

        self.private_key = Private_key(d, n)
        self.public_key = Public_key(e, n)

    def encode(self, plain_text):
        key = self.public_key
        return [pow(ord(x), key.e, key.n) for x in plain_text]

    def decode(self, cipher_text):
        key = self.private_key
        return ''.join([(chr(pow(x, key.d, key.n))) for x in cipher_text])
