import unittest
from unittest import mock

from Math import Math
from rsa import RSA, Public_key

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
        