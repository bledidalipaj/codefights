"""
This is a reverse challenge. No hints given :)

Have fun!

[time limit] 4000ms (py)
[input] integer n

Constraints:
1 ≤ n ≤ 12.

Input:
n: 1
Output:
2
Expected Output:
2

Input:
n: 2
Output:
5
Expected Output:
5

Input:
n: 3
Output:
12
Expected Output:
12

Input:
n: 4
Output:
34
Expected Output:
34

# Challenge's link: https://codefights.com/challenge/pvyQzct8QsRsAXoyZ/main #
"""
def addToFactorial(n):
    return math.factorial(n) + (n + 1) * n / 2