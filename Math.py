import string

import gmpy2
import random


class Math:
    """
    check x is prime number or not using Miller-Rabin algorithm
    """

    @staticmethod
    def isPrime(number: int):
        q = number - 1
        k = 0
        while q % 2 == 0:
            k += 1
            q = q / 2
        for i in range(50):
            a = random.randint(2, number - 2)
            x = pow(a, q, number)
            if x == 1 or x == number - 1:
                return False
            for j in range(k):
                x = pow(x, 2, number)
                if x == number - 1:
                    return False
        return True

    @staticmethod
    def getRandomNumber(bit_length: int):
        binary_string = '1'
        for x in range(bit_length - 2):
            a: int = random.randint(1, 100)
            binary_string += str(a % 2)
        binary_string += '1'
        num: int = int(gmpy2.mpz(binary_string, base=2))
        if Math.isPrime(num):
            return num
        else:
            Math.getRandomNumber(bit_length)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        pass

    """
    find two number p and q which have bit larger than min_number_of_bit
    res must return pair (p,q)
    """

    @staticmethod
    def find_p_and_q(min_number_of_bit=500) -> int:
        p: int = Math.getRandomNumber(min_number_of_bit)
        q: int = Math.getRandomNumber(min_number_of_bit)
        return p

    # Euclid extend
    @staticmethod
    def euclid_extend(e: int, m: int, dore: string) -> int:
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        q = int(m / e)
        r = m % e
        x = x0 - x1 * q
        y = y0 - y1 * q
        while r != 0:
            x = x0 - x1 * q
            y = y0 - y1 * q

            y0 = y1
            y1 = y

            x0 = x1
            x1 = x

            m = e
            e = r
            r = m % e
            q = int(m / e)
        if dore == 'd':
            return y
        else:
            if m * x + e * y == 1:
                return True
            else:
                return False

    """
    pick e, 1 < e < m which m = (p -1)(q-1)
    """

    @staticmethod
    def find_e(m: int) -> int:
        for i in range(m):
            if Math.euclid_extend(m, i, 'e') == 1:
                return i

    """
    e * d = 1 (mod m)
    """

    @staticmethod
    def find_d(e: int, m: int) -> int:
        return m + Math.euclid_extend(e, m, 'd')
