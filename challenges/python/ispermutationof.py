"""
Determines if leftString is a permutation (rearrangement of characters) of the rightString. If so, return true; otherwise return false.

Example

For leftString = "abc" and rightString = "bca", the output should be
IsPermutationOf(leftString, rightString) = true.

Input/Output

[time limit] 4000ms (py)
[input] string leftString

The left string to be checked.

[input] string rightString

The right string to be checked.

[output] boolean

Returns true if leftString is a permutation of rightString (and, of course, vice versa) and false otherwise.

# Challenge's link: https://codefights.com/challenge/SKpuysh7LNmHcRTax/main #
"""
def IsPermutationOf(leftString, rightString):
    return sorted(leftString) == sorted(rightString)