"""
A group of spies wants to hack a passcode of a safety box. The only possible way is to try every possible combination until the box is open. 
The spies want to calculate the number of possible combinations of the passcode to determine the estimated time and therefore plan accordingly.

Fortunately, they already know something about the passcode:

the passcode is an n-digit number;
if the ith digit is even, the (i + 1)th digit is odd;
if the ith digit is odd, the (i + 1)th digit is smaller than the ith one;
some of the digits are already known and are stored as knowndigits matrix.
Write a function that takes the passcode knowndigits and its length n and returns the total number of possible combinations.

Example

For knowndigits = [[1, 2], [3, 5]] and n = 5, the output should be
passwordHacking(knowndigits, n) = 38.

With the given constraints it is known that the passwords has the following format: 2X5XX, where X denotes unknown digits.

Here's what we know:

the 2nd digit can be odd and greater than 5, i.e. 2 options;
the 4th digit is smaller than 5, i.e. 5 options;
the 5th digit depends on the 4th one:
if the 4th digit is even, the 5th one can be any odd number, i.e. 5 options;
if the 4th digit equals 3, the 5th one can be any number less than 3, i.e. 3 options;
if the 4th digit equals 1, the 5th one can only be equal 0, i.e. 1 option.
Thus, the final answer can be calculated as follows:

Three possible combinations:
2 * 3 * 5 = 30
2 * 1 * 3 = 6
2 * 1 * 1 = 2
Their sum:
30 + 6 +2 = 38
Input/Output

[time limit] 4000ms (py)
[input] array.array.integer knowndigits

Each known digit is given as a pair [<position>, <digit>], where <position> is a 1-based index of the <digit>.

Constraints:
0 ≤ knowndigits.length < n,
1 ≤ <positioni> ≤ n,
<positioni> ≠ <positionj>,
0 ≤ <digiti> ≤ 9.

[input] integer n

The length of passcode.

Constraints:
2 ≤ n ≤ 10.

[output] integer

The total number of possible combinations.

# Challenge's link: https://codefights.com/challenge/W3G9JyaK5wkuvRTRA/main #
"""

def passwordHacking(knowndigits, n):

    knowndigits.sort(key = lambda tp: tp[0])
    ind = 0
    
    dp = []
    
    first_digits = [0] * 10
    if ind < len(knowndigits) and knowndigits[ind][0] == 1:
        first_digits[ knowndigits[ind][1] ] = 1
        ind += 1
    else:
        first_digits = [1] * 10
        
    dp.append(first_digits)
    
    for i in range(2, n + 1):
        cur_digits = []
        if ind < len(knowndigits) and knowndigits[ind][0] == i:
            restricted = True
            use_only = knowndigits[ind][1]
            ind += 1
        else:
            restricted = False
        for digit in range(10):
            num_combs = 0
            if not restricted or digit == use_only:
                for prev_digit, prev_combs in enumerate(dp[-1]):
                    if prev_digit % 2 == 0 and digit % 2 == 1 or \
                       prev_digit % 2 == 1 and digit < prev_digit:
                            num_combs += prev_combs
            cur_digits.append( num_combs )
        dp.append( cur_digits )
        
    return sum(dp[-1])


## Second Solution
from collections import defaultdict
def passwordHacking(knowndigits, n):
    d = {x[0]:x[1] for x in knowndigits}
    r={11:1}
    for i in xrange(1,n+1):
        tmp = defaultdict(int)
        for k in r:
            v = r[k]
            if k%2==0:
                for _ in range(1,10,2):
                    tmp[_]+=v
            else:
                for _ in range(min(k,10)):
                    tmp[_]+=v
        if i in d:
            r = {d[i]:tmp[d[i]]}
        else:
            r = tmp
    s = 0
    for ele in r:
        s+=r[ele]
    return s