"""
In recreational mathematics, a harshad number in a given number base is an integer that is divisible by the 
sum of its digits when written in that base. For example, 18 is a harshad number in base 10 because the sum 
of its digits (1 and 8) is 9, and 18 is divisible by 9. Harshad numbers were defined by D. R. Kaprekar, a 
mathematician from India.

You will be provided with 2 positive integers num1 and num2 (in base 10). Your mission is to calculate the 
value of the num2th harshad number modulo the num1th harshad number.

Example

For num1 = 12 and num2 = 20, the output should be
moduloHarshad(num1, num2) = 6.

The 20th harshad number is 42 and the 12th harshad number is 18. 42 % 18 is 6.

Input/Output

[time limit] 4000ms (py)
[input] integer64 num1

Constraints:
1 ≤ num1 ≤ 105.

[input] integer64 num2

Constraints:
1 ≤ num2 ≤ 105.

[output] integer64

The value of the num2th harshad number modulo the num1th harshad number

# Challenge's link: https://codefights.com/challenge/AWSp2cFm94tw4Eeeb #
"""
def moduloHarshad(num1, num2):
    def isHashard(num):
        total = 0
        tmp = num
        
        while tmp > 0:
            total += tmp % 10
            tmp /= 10
        return num % total == 0
            
    
    cnt = 0
    first = None 
    second = None
    
    i = 1
    while not first or not second:
        if isHashard(i):
            cnt += 1
            if cnt == num1:
                first = i 
            if cnt == num2:
                second = i 
        i += 1
        
    return second % first