"""
Have you ever heard of an IQ-address? For the given integer n, it is calculated as follows:

Let result = "".
If n = 1, prepend "1" to the beginning of result and return it as an answer.
Prepend n % 10.5 to the beginning of result.
Divide n by 2 with rounding up to the nearest integer.
Go to step 2.
Given an integer n, your task is to return IQ-address generated from it.

Example

For n = 21, the output should be
iqAddress(n) = "12.03.06.00.50.0".

Here's why:

21% 10.5 = 0.0
11% 10.5 = 0.5
6 % 10.5 = 6.0
3 % 10.5 = 3.0
2 % 10.5 = 2.0
Thus, the answer is "1"+"2.0"+"3.0"+"6.0"+"0.5"+"0.0" = "12.03.06.00.50.0".

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 105.

[output] string

The IQ-address generated from n.

# Challenge's link: https://codefights.com/challenge/Y7C33HX5SWeb8vEKd #

Round up a number
*****************
>>> int(21 / 5)
4
>>> int(21 / 5) + (21 % 5 > 0)
5

The first part becomes 4 and the second part evaluates to "True" if there is a remainder, which in addition True = 1; 
False = 0. So if there is no remainder, then it stays the same integer, but if there is a remainder it adds 1.
"""
def iqAddress(n):
    res = ""
    
    while True:
        if n == 1:
            res = "1" + res
            break
        else:
            res = `n % 10.5` + res
            n = math.ceil(n / 2.0)
    return res

def iqAddress(n):
    if n == 1:
        return "1"
    return iqAddress(math.ceil(n / 2.0)) + `n % 10.5`

def iqAddress(n):
	if n == 1:
		return "1"
	return iqAddress(n / 2 + n % 2 > 0) + `n % 10.5`

def iqAddress(n):
    return "1" if n == 1 else iqAddress(math.ceil(n / 2.0)) + `n % 10.5`

iqAddress = lambda n: "1" if n == 1 else iqAddress(math.ceil(n / 2.0)) + `n % 10.5`
iqAdress = lambda n: "1" if n == 1 else iqAddress(n / 2 + n % 2 > 0) + `n % 10.5`
iqAddress = v = lambda n: "1" if n == 1 else v(math.ceil(n / 2.0)) + `n % 10.5`