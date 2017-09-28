"""
Define the alternating digit sum of number "abc..xyz" as z - y + x - ... a, where a ... z are the digits the number consists of.

Given an integer n, your task is to find the alternating digit sum of n! and return it modulo 11.

Example

For n = 4, the output should be
AlternatingDigitSum(n) = 2.

4! = 24, its alternating digit sum is equal to 2, and 2 % 11 = 2, which is the answer.

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints
0 ≤ n ≤ 109.

[output] integer

The alternating digit sum of n! modulo 11.

# Challenge's link: https://codefights.com/challenge/uT2ywJR5QtJzJGqMb #
"""
def AlternatingDigitSum(n):
    res = 0
    sign = 1
    
    if n <= 10:
        fac = math.factorial(n)
        while fac > 0:
            res += (fac % 10) * sign 
            sign *= -1
            fac /= 10
    return res % 11

AlternatingDigitSum = lambda n: 0xa1525a26211>>n*4&15
AlternatingDigitSum = lambda n: n < 12 and math.factorial(n) % 11 or 0
AlternatingDigitSum = lambda n: 0 if n > 10 else math.factorial(n) %11
AlternatingDigitSum = lambda n: (n < 11) * (int('00151941409'[n % 11]) + 1)
AlternatingDigitSum = lambda n: [1, 1, 2, 6, 2, 10, 5, 2, 5, 1, 10][n] if n < 11 else 0