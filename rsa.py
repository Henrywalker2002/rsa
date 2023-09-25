from Math import Math
import math

class Private_key:

    def __init__(self, d: int, n: int):
        self.d = d
        self.n = n

    def __str__(self):
        return str(self.d) + ',' + str(self.n)

class Public_key:

    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n
        
    def __str__(self):
        return str(self.e) + ',' + str(self.n)


class RSA:

    def __init__(self, key_lengh = 1024):
        p, q = Math.find_p_and_q(int(key_lengh / 2))
        n = p*q
        m = (p-1)*(q-1)
        e = Math.find_e(m)
        d = Math.find_d(e, m)

        self.private_key = Private_key(d, n)
        self.public_key = Public_key(e, n)
        
    def get_private_key_str(self):
        return str(self.private_key)
    
    def get_public_key_str(self):
        return str(self.public_key)

    def encode(self, plain_text, public_key = None):
        key = public_key or self.public_key
        arr = bytes(plain_text, "utf-8")
        int_val = int.from_bytes(arr, 'big')
        encrypt = Math.mod_pow(int_val, key.e, key.n)
        return encrypt.to_bytes(int(encrypt.bit_length()  / 8) + 1, "big")

    def decode(self, cipher_text, private_key = None):
        key = private_key or self.private_key
        int_val = int.from_bytes(cipher_text, 'big')
        decrypt = Math.mod_pow(int_val, key.d, key.n)
        byte = decrypt.to_bytes(int(decrypt.bit_length() / 8) + 1, "big")
        return byte.decode("utf-8")

    @staticmethod
    def encrypt(plan_text, public_key):
        return RSA.encode(RSA, plan_text, public_key)
    
    @staticmethod
    def decrypt(cipher_text, private_key):
        return RSA.decode(RSA, cipher_text, private_key)