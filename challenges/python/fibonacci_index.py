"""
Consider the Fibonacci sequence: 0 1 1 2 3 5 8 13 21 ...

We can see that 7 is the smallest 0-based index k for which F(k) has exactly 
2 decimal digits.
What is the smallest index k for which F(k) has exactly n decimal digits?

Example

For n = 1, the output should be
fibonacciIndex(n) = 0;
For n = 2, the output should be
fibonacciIndex(n) = 7.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 10.

[output] integer

# Challenge's link: https://app.codesignal.com/challenge/F66Wq64Ne82betH2c #
"""

def fibonacciIndex(n):
	def fib_gen():
		a = 0
		b = 1

		while True:
			yield a 
			a, b = b, a + b 

	index = 0

	for num in fib_gen():
		if len(str(n)) == n:
			break 
		index += 1 
	return index 
