"""
Given a positive integer n, your task is to calculate the number of integers in the range [1, n] that have the same sum of digits as n.

Example

For n = 90, the output should be
SumOfDigits2(n) = 10.

There are 10 numbers in the range [1, 90] whose digits sum up to 9: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90.

Input/Output

[time limit] 4000ms (py)
[input] integer n

A positive integer.

Constraints:
1 ≤ n ≤ 109.

[output] integer

The result.

# Challenge's link: https://codefights.com/challenge/vkYYKvzo86rivfWLh/main #
"""

def memoize(f):
    memo = {}
    def result(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return result

@memoize
def count_digit_sum_distros(n, s):
    """Return number of sequences of 'n' digits that add up to 's'."""
    if n == 0:
        return 1 if s == 0 else 0
    else:
        result = 0
        for d in xrange(0, min(9, s) + 1):
            result += count_digit_sum_distros(n - 1, s - d)
        return result

def digits(n):
    """Return the digits of 'n'."""
    result = []
    while n > 0:
        n, r = divmod(n, 10)
        result.append(r)
    result.reverse()
    return result

def result_under(k, digits):
    if len(digits) == 1:
        return 1 if k <= digits[0] else 0
    result = 0
    for i in xrange(digits[0]):
        result += count_digit_sum_distros(len(digits) - 1, k)
        k -= 1
    result += result_under(k, digits[1:])
    return result

def SumOfDigits2(n):
    return result_under(sum(digits(n)), digits(n))


###################
# Second solution #
###################


def SumOfDigits2(n):
    return helper(sumd(n), n)

def helper(n, top):
    print("{} {}".format(n,top))
    if n == 0:
        return 1
    s = n
    count = 0
    if top < 1000:
        for i in range(top+1):
            if sumd(i) == s:
                count += 1
        return count
    
    c = [1 if i < 9 else 0 for i in range(s)]
    if len(c) == 0:
        return 0
    largest = int(math.log(top, 10)) + 1
    if s == 1:
        largest += 1
    
    isEnd = top == (10 ** largest) - 1
    if isEnd:
        largest += 1
    for i in range(1, largest):
        count += c[s-1]
        old = c[:]
        for i in range(9):
            old.insert(0,0)
            old.pop()
            for i in range(s):
                c[i] += old[i]
    if not isEnd:
        p = 10 ** (largest - 1)
        currentDigit = top / p
        for i in range(1, currentDigit):
            count += helper(n - i, p - 1)
        count += helper(n - currentDigit, top % p)
    
    return count

def sumd(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s