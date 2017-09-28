"""
Given an integer n, your task is to calculate the sum of digits in n! and return the answer modulo 9.

Example

For n = 4, the output should be
digitSumFactorial(n) = 6.

n! = 24, the sum of digits is 2 + 4 = 6, and 6 % 9 = 6. Thus, the output should be 6.

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
1 ≤ n ≤ 109.

[output] integer

The sum of digits in n! modulo 9.

# Challenge's link: https://codefights.com/challenge/G4MqZrhvDcG4uffSg #
"""

def digitSumFactorial(n):
	pass

digitSumFactorial = lambda n:126088 >> n * 3 & 7
digitSumFactorial = lambda n : [0, 1, 2, 6, 6, 3][n * (n < 6)]
digitSumFactorial= lambda n: [1,1,2,6,6,3,0][min(n,6)]
digitSumFactorial = lambda n: [1,1,2,6,6,3][n] if n < 6 else 0