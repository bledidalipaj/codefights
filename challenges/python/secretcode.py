"""
A spy is trying to crack a combination lock which has a numeric keypad with 10 digits on it. He knows that the code is an 8-digit number 
without leading zeros. He has also taken fingerprints from the pad to find out which buttons are pressed to enter the code. You know that 
a button has a fingerprint on it if and only if the digit on it is in the code.

What is the number of all possible code combinations that satisfy the information the spy has?

Example

For a = [false, true, false, false, false, false, false, false, false, false],
the output should be secretCode(a) = 1.

Since only one button has fingerprints on it (button 1), the code is definitely 11111111.

For a = [false, true, false, false, false, false, false, false, false, true],
the output should be secretCode(a) = 254.

The code consists of two digits, digit 1 and digit 9. There are 28 = 256 possible combinations of digits 1 and 9. However, 11111111 and 99999999 
are not valid combinations, since both digits must be present in it. Thus, the answer is 256 - 2 = 254.

Input/Output

[time limit] 12000ms (py)
[input] array.boolean a

A boolean array of length 10. a[i] is true if and only if the button with digit i has fingerprints on it.

[output] integer

The number of possible code combinations (0 if the provided information is contradictory).

# Challenge's link: https://codefights.com/challenge/gM5oqudpGvg8t36LN/main #
"""
import math

def binom(n, k):
    if 0 <= k <= n:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    else:
        return 0

CODE_LENGTH = 8

def code_count(button_count):
    result = 0
    n = button_count
    for i in xrange(n):
        result += (-1)**i * binom(button_count, i) * (n - i)**button_count
    return result

def memoize(f):
    memo = {}
    def result(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return result
    
@memoize
def opt(n, required_keys, optional_keys):
    if required_keys > n:
        return 0
    if n == 0:
        return 1
    result = 0
    result += opt(n - 1, required_keys - 1, optional_keys + 1) * required_keys
    result += opt(n - 1, required_keys, optional_keys) * optional_keys
    return result
    
def secretCode(a):
    button_count = sum(a)
    result = opt(8, button_count, 0)
    if a[0]:
        result -= opt(7, button_count - 1, 1)
    return result


def secretCode(a):
    f = math.factorial
    C = lambda x, y: f(x) / f(y) / f(x - y)
    
    def include_exclude(seq_len, usable, zero_used):
        res = 0
        for i in range(1, usable + 1):
            sign = -1 + 2 * (i & 1)
            num_intersections = C(usable, i)
            intersection_length = (usable - i) ** 8
            res += sign * num_intersections * intersection_length
        return res
            
    to_use = sum(a)
    total_combinations = (to_use - 1) * to_use ** 7 if a[0] \
                                                    else to_use ** 8
    total_combinations = to_use ** 8
    at_least_one_absent = include_exclude(8, to_use, a[0])
    print to_use, total_combinations, at_least_one_absent
    
    if to_use == 0:
        return 0
    if to_use == 1:
        return 1
    if a[0]:
        return (total_combinations - at_least_one_absent) *  (to_use - 1) / to_use
    return (total_combinations - at_least_one_absent)