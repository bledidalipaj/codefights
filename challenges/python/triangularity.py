"""
You have an array of integers, and each integer denotes the length of a segment. Determine whether it is possible 
to pick three segments and construct a triangle out of them.

It is possible to construct a triangle if the combined length of the two shortest segments is greater than the length 
of the longest segment.

Example

For segmentsLength = [1, 2, 3, 4], the output should be
triangularity(segmentsLength) = true.

The segments of lengths 2, 3, and 4 can be used to form a triangle.

For segmentsLength = [1, 2, 3], the output should be
triangularity(segmentsLength) = false.

The given three segments don't form a triangle.

Input/Output

[time limit] 4000ms (py)
[input] array.integer segmentsLength

An array of segment lengths.

Guaranteed constraints:
3 ≤ segmentsLength.length ≤ 105,
1 ≤ segmentsLength[i] ≤ 2 · 109.

[output] boolean

Return true if you can construct a triangle using three segments from segmentsLength, otherwise return false.

# Challenge's link: https://codefights.com/challenge/xunq4T96b3fY54Wif/solutions/z2Ye3ZEThNJxgme5j #
"""
def triangularity(segmentsLength):
    segmentsLength.sort()
    
    i = 0 
    j = 1 
    k = 2 
    while k < len(segmentsLength):
        if segmentsLength[i] + segmentsLength[j] > segmentsLength[k]:
            return True 
        i += 1
        j += 1
        k += 1
    return False


def triangularity(segmentsLength):
    segmentsLength.sort()

    res = False
    i = 0
    j = 1
    k = 2

    while k < len(segmentsLength):
        res = res or segmentsLength[i] + segmentsLength[j] > segmentsLength[k]
        i += 1
        j += 1
        k += 1
    return res

def triangularity(segmentsLength):
    segmentsLength.sort()
    res = 0

    for i in range(len(segmentsLength)):
        res += sum(segmentsLength[i - 2: i]) > segmentsLength[i]
    return res