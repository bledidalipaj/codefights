"""
You are given an array arr and 3 numbers - k, x and y. Your goal is to calculate unordered pairs of 
indices i and j such that:
i ≠ j, (arr[i] + arr[j]) % k = x and (arr[i] · arr[j]) % k = y (here % stands for modulo operation). 
Return the total number of pairs of indices that meet these requirements.

Example

For k = 2, x = 1, y = 0 and arr = [1, 2, 3, 2, 1], the output should be
unorderedPairsInArray(k, x, y, arr) = 6.

These 6 pairs of indices are: [0, 1], [0, 3], [1, 2], [1, 4], [2, 3], [3, 4].
For example, for pair [0, 1]: (1 + 2) % 2 = 1 and (1 * 2) % 2 = 0.

Input/Output

[time limit] 4000ms (py)
[input] integer k

Constraints:
1 ≤ k ≤ 109.

[input] integer x

Constraints:
0 ≤ x ≤ k.

[input] integer y

Constraints:
0 ≤ y ≤ k.

[input] array.integer arr

Constraints:
0 ≤ arr.length ≤ 1000,
0 ≤ arr[i] ≤ 105.

[output] integer
"""
def unorderedPairsInArray(k, x, y, arr):
    res = 0
    ln = len(arr)
    
    for i in range(ln):
        for j in range(i + 1, ln):
            if (arr[i] + arr[j]) % k == x and (arr[i] * arr[j]) % k == y:
                res += 1
    return res