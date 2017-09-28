"""
You have a calculator called BiCalc, which is very strange, as it can only perform two operations: multiply by 2, denoted as x2, and subtract 
by 1, denoted -1. You have a lot of time on your hands, so write a program that will help you determine the minimum number of button presses 
required to get from the start value to the end value.

Other important information

The calculator can only display numbers up to 999999999 = 109 - 1, so if at any time the current value of the number becomes greater than 
999999999, the calculator will display "Error".

It is guaranteed that there is no need to use negative numbers to solve this challenge.

Examples

For start = 1 and end = 16, the output should be
BiCalc(start, end) = 4.

You can multiply 1 by 2 four times to get 16 (i.e. press x2 4 times).

For start = 8 and end = 2, the output should be
BiCalc(start, end) = 6.

You can subtract 1 from 8 six times to get 2 (i.e. press -1 6 times).

Input/Output

[time limit] 4000ms (js)
[input] integer start

The starting number that is displayed on the calculator.

Constraints:
1 ≤ start ≤ 109 - 1.

[input] integer end

The number that you wish to achieve with as few button presses as possible.

Constraints:
1 ≤ end ≤ 109 - 1.

[output] integer

The minimum number of button presses required to get from start to end or return -1 (the integer, not the button) if it isn't possible.

# Challenge's link: https://codefights.com/challenge/4qomB9ThTehgbra72/main #
"""
def BiCalc(start, end):
    result = 0
    while start != end:
        if end >= 10**9:
            return -1
        if start >= end:
            result += start - end
            end = start
        elif end % 2 == 1:
            end += 1
            result += 1
        else:
            end /= 2
            result += 1
    return result

def BiCalc(start, end):
    res = 0
    while end > start:
        if end % 2 != 0:
            end += 1
        else:
            end /= 2
        if end >= 10**9: return -1
        res += 1
    return  res + s - e