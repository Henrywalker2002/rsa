import unittest
from unittest import mock

from Math import Math
from rsa import RSA

class unittest(unittest.TestCase):
    
    def setUp(self):
        pass 
    
    def test_is_prime(self):
        self.assertEqual(Math.isPrime(11), True)
        self.assertEqual(Math.isPrime(15), False)
        
    def test_random_number(self):
        self.assertGreater(Math.getRandomNumber(), pow(2, 499))
        self.assertEqual(Math.isPrime(Math.getRandomNumber()), True) 
        
    def test_euclid_extend(self):
        self.assertEqual(Math.find_d(7, 160), 23)
        
    def test_find_e(self):
        temp = Math.find_e(160)
        self.assertEqual(True, Math.gcd(temp, 160) == 1)

    def test_rsa(self):
        rsa = RSA()
        cipher = rsa.encode("hello")
        self.assertEqual(rsa.decode(cipher), "hello")
        
    def test_rsa_encode(self):
        rsa = mock.Mock()
        public_key = mock.Mock()
        public_key.e = 7
        public_key.n = 187
        rsa.public_key = public_key
        self.assertEqual(RSA.encode(rsa, 'X'), [11])

    def test_rsa_decode(self):
        rsa = mock.Mock()
        
        private_key = mock.Mock()
        private_key.d = 23
        private_key.n = 187
        rsa.private_key = private_key
        
        self.assertEqual(RSA.decode(rsa, [11]), 'X')