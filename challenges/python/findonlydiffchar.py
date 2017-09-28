"""
You created an awesome array a, but some hooligan removed one element from it, shuffled it and returned it to 
you as array b.

Given arrays a and b, your task is to figure out what element was removed from a.

Example

For a =[1, 2, 3, 4] and b = [3, 1, 2],
the output should be
findOnlyDiffChar(a, b) = 4.

[time limit] 4000ms (py)
[input] array.integer a

Constraints:
1 ≤ a.length ≤ 4000,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array consisting of exactly the same elements as a, except for a single missing element.

Constraints:
b.length = a.length - 1.

[output] integer

The missing element.

# Challenge's link: https://codefights.com/challenge/RsQYfmimvek4JiiiG #
"""
def findOnlyDiffChar(a, b):
	res = 0

	for num in a + b:
		res ^= num 
	return res

findOnlyDiffChar = lambda a, b: reduce(lambda x, y: x ^ y, a + b)
findOnlyDiffChar = lambda a, b: sum(a) - sum(b)