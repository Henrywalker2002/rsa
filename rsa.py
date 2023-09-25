from Math import Math
import math

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
        arr = bytes(plain_text, "utf-8")
        int_val = int.from_bytes(arr, 'big')
        key = self.public_key
        encrypt = Math.mod_pow(int_val, key.e, key.n)
        return encrypt.to_bytes(int(encrypt.bit_length()  / 8) + 1, "big")

    def decode(self, cipher_text):
        key = self.private_key
        int_val = int.from_bytes(cipher_text, 'big')
        decrypt = Math.mod_pow(int_val, key.d, key.n)
        byte = decrypt.to_bytes(int(decrypt.bit_length() / 8) + 1, "big")
        return byte.decode("utf-8")
