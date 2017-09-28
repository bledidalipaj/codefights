"""
Given an integer n, you can remove either its first or last digit in one step. After applying this operation 
several times, you'll get a number x with a length of k. It's possible that the number will contain leading zeros. 
What is the minimal and the maximal possible value of x that you can obtain?

Example

For n = 15243 and k = 2, the output should be
removeDigits(n, k) = [15, 52].

To obtain the minimal number with a length of k, we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 15;
To obtain the maximal number with a length of k, we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 52.
For n = 123 and k = 1, the output should be
removeDigits(n, k) = [1, 3].

Input/Output

[time limit] 4000ms (py3)
[input] integer64 n

The initial number.

Guaranteed constraints:
10 ≤ n ≤ 1015.

[input] integer k

The desired length of the output number.

Guaranteed constraints:
1 < 10k ≤ n.

[output] array.integer64

An array in which the first element is equal to the minimal possible number with length k and the second element is equal 
to the maximal possible number of length k.

# Challenge's link: https://codefights.com/challenge/mYSs9Exk9t7YCmfua/ #
"""
def removeDigits(n, k):
    digits = list(str(n))
    nums = []
    
    for i in range(len(digits) - k + 1):
        nums.append(int("".join(digits[i: i + k])))
    return (min(nums), max(nums))

removeDigits = f = lambda n, k: n < 10 ** k and [n, n] or sorted(f(n / 10, k) + [n % 10 ** k])[::2]

def removeDigits(n,k):
    t = []
    k = 10 ** k
    while n * 10 / k:
        t += n % k,
        n /= 10
    return min(t), max(t)