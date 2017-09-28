"""
You are given two non-negative integers, number1 and number2, given in bases base1 and base2, respectively. Each 
base can be in range from Binary (2) to Hexatridecimal (36).

Your task is to sum the given numbers and return them in one of the given bases. Here's how the base of the returned value is determined:

if number1 ≠ number2, the base of the largest number should be chosen;
if number1 = number2, the largest base from the given should be chosen.
Note, that characters used in bases greater than 10 are given in the lowercase.

For your convenience, you can check out this base number converter or this converter.

Example

BaseAdd("11", 2, "10", 10) = "13".

112 = 310, thus the sum equals 3 + 10 = 1310. Since 112 < 1010, base 10 should be used in the answer.

BaseAdd("11111100000", 2, "7e0", 16) = "fc0".

111111000002 = 201610, and 7e016 = 201610 as well. Thus the sum equals 2016 + 2016 = 403210. number1 = number2, the largest 
base should be used in the answer, which is 16. So, the answer is 403210 = fc016.

Input/Output

[time limit] 4000ms (py)
[input] string number1

The first number.

Constraints:
0 ≤ int(number1) < 253 (MAX_SAFE_INTEGER).

[input] integer base1

Base of the first number.

Constraints:
2 ≤ base1 ≤ 36.

[input] string number2

The second number.

Constraints:
0 ≤ int(number2) < 253 (MAX_SAFE_INTEGER).

[input] integer base2

Base of the second number.

Constraints:
2 ≤ base2 ≤ 36.

[output] string

The answer. It is guaranteed that it will be smaller than 253.

# Challenge's link: https://codefights.com/challenge/rXBQajNqcNeqx32Mz #
"""
def BaseAdd(number1, base1, number2, base2):
    def base_converter(decimal, base):
        res = ""
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        
        while decimal > 0:
            res = digits[decimal % base] + res 
            decimal /= base 
        return res
    
    dec_number1 = int(number1, base1)
    dec_number2 = int(number2, base2)
    
    if dec_number1 > dec_number2:
        chosen_base = base1
    elif dec_number1 < dec_number2:
        chosen_base = base2
    else:
        chosen_base = max(base1, base2)
    
    res = dec_number1 + dec_number2
    
    return base_converter(res, chosen_base)