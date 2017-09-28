"""
This is a reverse challenge. Enjoy!

[time limit] 4000ms (py)
[input] array.integer lst

Constraints:
0 ≤ lst.length ≤ 1500,
0 ≤ lst[i] ≤ 231.

Input:
lst: [1]
Output:
Empty
Expected Output:
1

Input:
lst: [1, 6, 3, 9, 36]
Output:
Empty
Expected Output:
10

Input:
lst: [7, 11, 16, 64, 49, 4, 8, 121]
Output:
Empty
Expected Output:
30

Input:
lst: [50, 37, 85, 44, 32, 13, 85, 89, 79, 50, 73, 20, 47, 6, 74, 29, 10, 8, 89, 57]
Output:
Empty
Expected Output:
0

Input:
lst: [2, 3, 2, 4, 5, 9, 9]
Output:
Empty
Expected Output:
7

# Challenge's link: https://codefights.com/challenge/C3PNZHBXqFEi6hdQn #
"""
def SumSquareRoot(lst):
    res = 0
    used = []
    
    for num in lst:
        square_root = num ** 0.5
        if float(int(square_root)) == square_root and square_root not in used:
            res += square_root * (lst.count(square_root))
            used.append(square_root)
    return res

# python3
def SumSquareRoot(lst):
    res = 0
    
    for num in set(lst):
        sqrt = num ** .5
        
        if int(sqrt) == sqrt:
            res += sqrt * lst.count(sqrt)
    return res

def SumSquareRoot(lst):
    res = 0
    was = set()
    for i in lst:
        s = i ** .5
        if s.is_integer() and s not in was:
            res += lst.count(s) * s
            was.add(s)
    return res

def SumSquareRoot(lst):

    total = 0
    for n in lst:
        if (n * n in lst):
            total = total + n
    return total

SumSquareRoot = lambda lst: sum(x for x in lst if x * x in lst)