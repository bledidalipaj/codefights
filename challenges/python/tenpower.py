"""
Given a list of numbers, your task is to find all its elements that are not smaller than 10. The result you should return can be found from 
these values as follows:

the tens of the ith (0-based) found value should be added to the result if i is even;
the tens of the ith (0-based) found value should be subtracted from the result if i is odd.
Example

For numbers = [9, 10, 6, 3, 24, 0, 7], the output should be
TenPower(numbers) = -1.

There are two numbers than are not smaller than 10: 10 and 24. The result can thus be obtained as 1 - 2 = -1.

Input/Output

[time limit] 4000ms (py)
[input] array.integer numbers

Constraints:
0 ≤ numbers.length ≤ 1500,
0 ≤ numbers[i] < 231.

# Challenge's link: https://codefights.com/challenge/xm9eDrzYWvz7EL4Pp #
"""
def TenPower(numbers):
    res = 0
    values_found = 0
    
    for number in numbers:
        if number > 9:
            if values_found % 2 == 0:
                res += (number % 100) / 10
            else:
                res -= (number % 100) / 10
            values_found += 1
    return res

def TenPower(lst):
    res = 0
    cnt = 0
    for i in lst:
        if i > 9:
            res += (-1) ** cnt * (i // 10 % 10)
            cnt += 1
    return res