"""
Jack and Naomi found a big jar with candies that they want to split. Both of them love prime numbers, so they are wondering if the candies can 
be split so that each kid gets a prime number of candies.

Given the number of candies n, your task is to help them: return true if the candies can be split as Jack and Naomi want to, and false otherwise.

Example

For n = 18, the output should be
Candies(n) = true.

It is possible to split 18 as 18 = 7 + 11, since 7 and 11 are both primes.

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
4 ≤ n < 8 · 105.

[output] boolean

true if n candies can be split int to groups of prime number of candies, false otherwise.

# Challenge's link: https://codefights.com/challenge/RTqP9TWA3NNoyuuaf #
"""
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def Candies(n):
    # According to Goldbach's conjecture: any even number can be written
    # as the sum of two prime numbers. 
    # 
    # Therefore  if n is even we return true.
    # 
    # If n is odd, in order for n to be written as the sum of two primes, 
    # one of the primes should be 2 (because the sum of 2 with any prime number 
    # gives us an odd number, on the other hand the sum of two prime numbers results 
    # in an even number), so we only need to check if n - 2 is prime.
    # Therefore if n - 2 is prime we return true otherwise we return false.
    if n % 2 == 0 or is_prime(n - 2):
        return True 
    return False

# probabilistic solution, see https://en.wikipedia.org/wiki/Fermat_primality_test
Candies = lambda n: n % 2 * pow(39, n - 3, n - 2) < 2

Candies = lambda n: n%2==0 or all((n-2)%i for i in range(2,n/2))