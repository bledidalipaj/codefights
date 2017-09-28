"""
Given two positive integers a and b, return the bitwise XOR of all the integers in range [a, b].

Example

For a = 2 and b = 4, the output should be
rangeXOR(a, b) = 5.

Here's why:

210 ^ 310 ^ 410 = 0102 ^ 0112 ^ 1002 = 1012 = 510.

Input/Output

[time limit] 4000ms (py)
[input] integer a

Constraints:
0 ≤ a < b.

[input] integer b

Constraints:
a < b ≤ 2 · 109.

[output] integer

# Challenge's link: https://codefights.com/challenge/KEbTTLutFqbTvs4mu #
"""
def rangeXOR(a, b):
	pass


def rangeXor(a, b):
	f = lambda x: [x, 1, x + 1, 0][x % 4]
	return f(b) ^ f(a - 1)