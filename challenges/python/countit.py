"""
This problem can be solved by pre-school children in 5-10 minutes. By programmers in one hour. By people with a 
higher education… Well, it certainly can take them a while.

Since you, CodeFighters, are supposed to be programmers, it shouldn't take you that long to solve it :) Take a 
look at the test cases and figure what this is all about.

Beware the corner cases!

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 230

[output] integer

Input:
n: 8809
Output:
Empty
Expected Output:
6

Input:
n: 7111
Output:
Empty
Expected Output:
0

Input:
n: 1234
Output:
Empty
Expected Output:
0

Input:
n: 6666
Output:
Empty
Expected Output:
4

# Challenge's link: https://codefights.com/challenge/v5Zg8trjoun3PTxrZ/ #
"""
def countIt(n):
    res = 0
    tmp = n
    while tmp > 0:
        digit = tmp % 10
        if digit in [0, 6, 9]:
            res += 1
        if digit == 8:
            res += 2
        tmp /= 10
    return res if n > 0 else 1

countIt = lambda n:sum(map(`n`.count, "06889"))