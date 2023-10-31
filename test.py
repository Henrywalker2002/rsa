import unittest
from unittest import mock

from Math import Math
from rsa import RSA, Public_key

from math import sqrt

def isPrime(n):
     
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
     
    k = int(sqrt(n)) + 1
    for i in range(5, k, 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
 
    return True
 
# Function that returns true if 
# n is a strong prime
def isStrongPrime(n):
     
    # If n is not a prime number or
    # n is the first prime then return false
    if (isPrime(n) == False or n == 2):
        return False
 
    # Initialize previous_prime to n - 1
    # and next_prime to n + 1
    previous_prime = n - 1
    next_prime = n + 1
 
    # Find next prime number
    while (isPrime(next_prime) == False):
        next_prime += 1
 
    # Find previous prime number
    while (isPrime(previous_prime) == False):
        previous_prime -= 1
 
    # Arithmetic mean
    mean = (previous_prime + next_prime) / 2
 
    # If n is a strong prime
    if (n > mean):
        return True
    else:
        return False

class unittest(unittest.TestCase):
    
    # def setUp(self):
    #     pass 
    
    # def test_is_prime(self):
    #     self.assertEqual(Math.isPrime(11), True)
    #     self.assertEqual(Math.isPrime(15), False)
        
    # def test_random_number(self):
    #     self.assertGreater(Math.getRandomNumber(), pow(2, 499))
    #     self.assertEqual(Math.isPrime(Math.getRandomNumber()), True) 
        
    # def test_euclid_extend(self):
    #     self.assertEqual(Math.find_d(7, 160), 23)
        
    # def test_find_e(self):
    #     temp = Math.find_e(160)
    #     self.assertEqual(True, Math.gcd(temp, 160) == 1)

    # def test_rsa(self):
    #     rsa = RSA()
    #     cipher = rsa.encode("hello")
    #     self.assertEqual(rsa.decode(cipher), "hello")
        
    def test_strong_prime(self):
        num = Math.generate_strong_prime_number()
        self.assertTrue(Math.isPrime(num))
        self.assertTrue(isStrongPrime(num))
        
        