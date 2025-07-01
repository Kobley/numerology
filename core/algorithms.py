from core.strCon import strConstants

def entry() -> None:
    raise RuntimeError(strConstants.INCORRECT_USAGE)

if __name__ == "__main__":
    entry()

import math

SMALL_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463
]

class alg:

    @staticmethod
    def check_prime_factors(n) -> bool:
        for p in SMALL_PRIMES:
            if n % p == 0:
                return False
        return True

    @staticmethod
    def miller_rabin(n, k=5):
        """Miller-Rabin primality test. Returns True if n is probably prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        # Write n-1 as 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            d //= 2
            r += 1

        import random
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    @staticmethod
    def nth_fib(n):
        """Returns the nth Fibonacci number using fast doubling."""
        def fib_pair(n):
            if n == 0:
                return (0, 1)
            else:
                a, b = fib_pair(n // 2)
                c = a * (2 * b - a)
                d = a * a + b * b
                if n % 2 == 0:
                    return (c, d)
                else:
                    return (d, c + d)
        return fib_pair(n)[0]

    @staticmethod
    def is_fibonacci(num):
        """Checks if num is a Fibonacci number."""
        def is_perfect_square(x):
            s = int(x ** 0.5)
            return s * s == x
        return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

    @staticmethod
    def nth_prime(n):
        """Returns the nth prime number using a sieve for small n, or a segmented sieve for larger n."""
        if n < 1:
            raise ValueError("n must be >= 1")
        # Use a rough upper bound for nth prime: n*log(n) + n*log(log(n))
        if n < 6:
            upper = 15
        else:
            upper = int(n * (math.log(n) + math.log(math.log(n)))) + 10
        sieve = [True] * (upper + 1)
        sieve[0:2] = [False, False]
        count = 0
        for i in range(2, upper + 1):
            if sieve[i]:
                count += 1
                if count == n:
                    return i
                for j in range(i * i, upper + 1, i):
                    sieve[j] = False
        # If not found, increase upper and try again (rare for very large n)
        raise ValueError("n is too large for this method")

    @staticmethod
    def is_twin_prime(n):
        """Checks if n is a twin prime."""
        if not alg.miller_rabin(n):
            return False
        return alg.miller_rabin(n - 2) or alg.miller_rabin(n + 2)

    @staticmethod
    def is_safe_prime(n):
        """Checks if n is a safe prime (i.e., n is prime and (n-1)//2 is also prime)."""
        if not alg.miller_rabin(n):
            return False
        return alg.miller_rabin((n - 1) // 2)

    @staticmethod
    def is_primitive_root(g, p):
        """Checks if g is a primitive root modulo p (p must be prime)."""
        if not alg.miller_rabin(p):
            return False
        phi = p - 1
        # Find all prime factors of phi
        factors = set()
        d = phi
        i = 2
        while i * i <= d:
            if d % i == 0:
                factors.add(i)
                while d % i == 0:
                    d //= i
            i += 1
        if d > 1:
            factors.add(d)
        for q in factors:
            if pow(g, phi // q, p) == 1:
                return False
        return True

    @staticmethod
    def is_sophie_germain_prime(p):
        """Checks if p is a Sophie Germain prime."""
        return alg.miller_rabin(p) and alg.miller_rabin(2 * p + 1)

    @staticmethod
    def is_palindromic(n):
        """Checks if n is a palindromic"""
        return str(n) == str(n)[::-1]

    @staticmethod
    def is_perfect_number(n):
        """Checks if n is a perfect number."""
        if n < 2:
            return False
        divisors_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum == n

    @staticmethod
    def is_square(n):
        """Checks if n is a perfect square."""
        if n < 0:
            return False
        root = int(n ** 0.5)
        return root * root == n

    @staticmethod
    def is_cube(n):
        """Checks if n is a perfect cube."""
        if n < 0:
            root = int(round(abs(n) ** (1/3)))
            return -root * root * root == n
        root = int(round(n ** (1/3)))
        return root * root * root == n

    @staticmethod
    def squares_in_range(start, end):
        """Returns a list of all perfect squares in [start, end] (inclusive)."""
        result = []
        n = int(start ** 0.5)
        if n * n < start:
            n += 1
        while n * n <= end:
            result.append(n * n)
            n += 1
        return result

    @staticmethod
    def primes_up_to(n):
        """Returns a list of all primes <= n using the Sieve of Eratosthenes."""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    @staticmethod
    def segmented_sieve(limit):
        """Returns a list of all primes <= limit using the segmented sieve."""
        import math
        if limit < 2:
            return []
        sqrt = int(math.sqrt(limit)) + 1
        primes = alg.primes_up_to(sqrt)
        result = primes.copy()
        low = sqrt
        high = 2 * sqrt
        while low < limit + 1:
            if high > limit + 1:
                high = limit + 1
            mark = [True] * (high - low)
            for p in primes:
                # Find the minimum number in [low, high) that is a multiple of p
                start = max(p * p, ((low + p - 1) // p) * p)
                for j in range(start, high, p):
                    mark[j - low] = False
            for i in range(low, high):
                if mark[i - low]:
                    result.append(i)
            low += sqrt
            high += sqrt
        return result

    @staticmethod
    def contains_digit_substring(n, substring):
        """Checks if the digit sequence 'substring' is contained in the decimal representation of n."""
        return substring in str(abs(n))

    @staticmethod
    def has_repeated_digits(n):
        """Checks if n has any repeated digits."""
        s = str(abs(n))
        return len(set(s)) < len(s)

    @staticmethod
    def has_palindromic_substring(n, length):
        """Checks if n contains a palindromic substring of the given length."""
        s = str(abs(n))
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub == sub[::-1]:
                return True
        return False

    @staticmethod
    def digit_sum(n):
        """Returns the sum of the digits of n."""
        return sum(int(d) for d in str(abs(n)))

    @staticmethod
    def digital_root(n):
        """Returns the digital root of n."""
        n = abs(n)
        while n >= 10:
            n = sum(int(d) for d in str(n))
        return n

    @staticmethod
    def sum_of_divisors(n):
        """Returns the sum of all positive divisors of n (including n)."""
        if n < 1:
            return 0
        total = 1 + n if n > 1 else 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total

    @staticmethod
    def sum_of_prime_divisors(n):
        """Returns the sum of all distinct prime divisors of n."""
        if n < 2:
            return 0
        s = 0
        x = n
        for p in SMALL_PRIMES:
            if x % p == 0:
                s += p
                while x % p == 0:
                    x //= p
        f = 2 if x % 2 else 3
        while x > 1 and f * f <= x:
            if x % f == 0:
                if alg.miller_rabin(f):
                    s += f
                while x % f == 0:
                    x //= f
            f += 2
        if x > 1:
            s += x
        return int(s)

    @staticmethod
    def prime_factors(n):
        """Returns a list of the prime factors of n (with multiplicity)."""
        if n < 2:
            return []
        factors = []
        x = n
        for p in SMALL_PRIMES:
            while x % p == 0:
                factors.append(p)
                x //= p
        f = 2 if x % 2 else 3
        while x > 1 and f * f <= x:
            while x % f == 0:
                if alg.miller_rabin(f):
                    factors.append(f)
                x //= f
            f += 2
        if x > 1:
            factors.append(x)
        return factors

    @staticmethod
    def fib_index(num):
        """Returns the index n such that Fibonacci(n) == num, or -1 if not a Fibonacci number."""
        if num < 0:
            return -1
        a, b = 0, 1
        idx = 0
        while a < num:
            a, b = b, a + b
            idx += 1
        return idx if a == num else -1

    @staticmethod
    def fibs_up_to(n):
        """Returns a list of all Fibonacci numbers <= n."""
        fibs = []
        a, b = 0, 1
        while a <= n:
            fibs.append(a)
            a, b = b, a + b
        return fibs

    @staticmethod
    def first_n_fibs(n):
        """Returns a list of the first n Fibonacci numbers."""
        if n < 1:
            return []
        fibs = [0]
        if n == 1:
            return fibs
        fibs.append(1)
        for _ in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs