"""
This is a reverse challenge, enjoy!

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n < 231

[output] boolean

Input:
n: 0
Expected Output:
true

Input:
n: 1
Expected Output:
false

Input:
n: 3
Expected Output:
false

Input:
n: 19
Expected Output:
true

Input:
n: 91
Expected Output:
false

Input:
n: 10
Expected Output:
false

Input:
n: 27
Expected Output:
true

# Challenge's link: https://codefights.com/challenge/enM8nziGuNuGjSxPg #
"""
def one1(n):
    """
    Check Codes
    ***********
    There are many places in our lives where we meet identification numbers; for example, passports, 
    bank accounts, credit cards, ISBN book numbers, and so on. Each identification number obeys a rule 
    which makes it easy to check (most of the time) whether the number has been copied correctly or not 
    and for this reason they are also called check codes. Here are some of the methods for checking the 
    validity of these numbers. They use modulus or clock arithmetic.

    ISBN Numbers : Books have ten digit identification numbers a1⋯a10 using the digits 0 to 9 where

	10a1+9a2+8a3+...+3a8+2a9+a10 = 0\ mod 11.

	Sometimes this forces the check-digit a10 to be 10; as this would then give an eleven digit number the 
	publishers use X instead of 10. For example, to check
	0 7167 2393 X we calculate 0+63+8+42+42+10+12+27+6=210 so, as the check digit is 10 which makes the total 
	220 (a multiple of 11) we know this is a valid ISBN number.

	source: https://nrich.maths.org/2036
    """
    digits = map(int, str(n))
    weighted_sum = 0
    weight = len(digits)
    
    for i in range(len(digits) - 1):
        weighted_sum += digits[i] * weight 
        weight -= 1
    return (weighted_sum + digits[-1]) % 11 == 0