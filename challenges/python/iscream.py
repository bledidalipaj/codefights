"""
This is a reverse challenge, enjoy!

Input/Output

[time limit] 4000ms (py)
[input] integer flavors

Constraints:
1 ≤ flavors ≤ 15.

[input] integer scoops

Constraints:
0 ≤ scoops ≤ 15.

[output] integer

Input:
flavors: 5
scoops: 3
Expected Output:
35

Input:
flavors: 3
scoops: 3
Expected Output:
10
"""
f = math.factorial
def iScream(flavors, scoops):
    return f(flavors + scoops - 1) / (f(flavors - 1) * f(scoops))