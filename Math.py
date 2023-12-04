import random


class Math:

    @staticmethod
    def mod_pow(base, e, m = None):
        res = 1
        
        while e > 0:
            
            if e % 2 != 0:
                res = res * base % m if m else res * base
            
            e = e >> 1 # e = e /2 
            base = base * base % m if m else base * base
        
        return res % m if m else res
    
    @staticmethod
    def isPrime(n, k = 50):
        """
        check x is prime number or not using Miller-Rabin algorithm
        """
        if n == 2:
            return True

        if n % 2 == 0:
            return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = Math.mod_pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = Math.mod_pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    
    @staticmethod 
    def generate_strong_prime_number(bit_length : int = 512):
        s = Math.getRandomPrimeNumber(int(bit_length/2))
        t = Math.getRandomPrimeNumber(int(bit_length/2))
        
        count = 1 
        r = 2 * count * t + 1
        while not Math.isPrime(r):
            count += 1 
            r = 2 * count * t + 1 
        
        p0 = 2 * (Math.mod_pow(s, r - 2 , r))*s - 1 
        count = 1 
        p = p0 + 2 * count * r *s 
        while not Math.isPrime(p):
            count += 1 
            p = p0 + 2 * count * r *s 
        return p 
        
    @staticmethod
    def getRandomPrimeNumber(bit_length: int = 500):
        binary_string = '1'
        for x in range(bit_length - 2):
            a: int = random.randint(1, 100)
            binary_string += str(a % 2)
        binary_string += '1'
        num: int = int(binary_string, 2)
        if Math.isPrime(num):
            return num
        else:
            return Math.getRandomPrimeNumber(bit_length)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        if a == 0:
            return b
    
        return Math.gcd(b % a, a)

    @staticmethod
    def find_p_and_q(min_number_of_bit=512) -> int:
        """
        find two number p and q which have bit larger than min_number_of_bit
        res must return pair (p,q)
        """
        p: int = Math.generate_strong_prime_number(min_number_of_bit)
        q: int = Math.generate_strong_prime_number(min_number_of_bit)
        return (p,q)

    # Euclid extend
    @staticmethod
    def euclid_extend(e: int, m: int, dore: str) -> int:
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        q = int(m // e)
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
            q = int(m // e)
        if dore == 'd':
            return y
        else:
            if m * x + e * y == 1:
                return True
            else:
                return False


    @staticmethod
    def find_e(m: int) -> int:
        """
        pick e, 1 < e < m which m = (p -1)(q-1)
        """
        a = []
        # min, max = random.uniform(0.000001, 1/3), random.uniform(2/3, 1)
        for i in range( m // 3, m):
            if Math.gcd(m, i) == 1:
                a.append(i) 
            if len(a) == 50:
                break
        return a[random.randint(0, len(a) - 1)]

    @staticmethod
    def find_d(e: int, m: int) -> int:
        """
        e * d = 1 (mod m)
        """
        return (m + Math.euclid_extend(e, m, 'd')) % m 
