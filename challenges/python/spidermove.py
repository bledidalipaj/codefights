"""
A spider is standing at the origin (0, 0) of a Cartesian plane and wants to move to the point (X,Y). At each step, the spider can only move one 

square in two of the four directions: U(up), D(down,), L(left), R(right), depending on where it is heading:

if X ≥ 0, Y ≥ 0. The spider can only go U or R.
if X ≥ 0, Y ≤ 0. The spider can only go D or R.
if X ≤ 0, Y ≥ 0. The spider can only go U or L.
if X ≤ 0, Y ≤ 0. The spider can only go D or L.
Find the number of ways for the spider to get to the given point (X, Y).

Example

For X = 2 and Y = -2, the output should be
spiderMove(X, Y) = 6.

There are only 6 ways:

RRDD;
RDRD;
RDDR;
DRRD;
DRDR;
DDRR.
For X = -3 and Y = 0, the output should be
spiderMove(X, Y) = 1.

There is only one way:

LLL.
For X = 0 and Y = 0, the output should be
spiderMove(X, Y) = 1.

Input/Output

[time limit] 4000ms (py)
[input] integer X

Constraints:
-15 ≤ X ≤ 15.

[input] integer Y

Constraints:
-5 ≤ Y ≤ 25.

[output] integer

It is guaranteed that the answer is smaller than 231.

# Challenge's link: https://codefights.com/challenge/uyyGtj8e3oH5gGWPz/main #
"""

def spiderMove(X, Y):
	"""
		Lattice paths
		source: http://math.stackexchange.com/questions/103480/number-of-ways-of-reaching-a-point-from-origin
	"""
    x = abs(X)
    y = abs(Y)
    
    res = math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
    
    return res

def spiderMove(X, Y):

    X = abs(X)
    Y = abs(Y)

    n = []
    for i in range(X + 1):
        n.append(1)

    for i in range(Y):
        for j in range(1, X + 1):
            n[j] = n[j - 1] + n[j]

    return n[X]

spiderMove = r = lambda X, Y: X * Y and r(abs(X) - 1,Y) + r(X, abs(Y)  -1) or 1