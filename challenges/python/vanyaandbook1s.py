"""
Vanya got an important task — he should enumerate the books in the library and label each book with its number. 
Each of the n books should be assigned with a number from 1 to n. Naturally, each book should have a unique number.

Vanya wants to know how many digits he will have to write down as he labels the books. Your task is to help him!

Example

For n = 13, the output should be
VanyaAndBook1s(n) = 17.

The books should be labeled with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, which totals to 17 digits.

Input/Output

[time limit] 4000ms (py3)
[input] integer n

The number of books in the library.

Constraints:
1 ≤ n ≤ 108.

[output] integer

The number of digits that Vasya needs to write down in order to label all the books.

# Challenge's link: https://codefights.com/challenge/xkEsQ3fYxMHwtvFMG #
"""
def VanyaAndBook1s(n):
    # 1-9-> (9 - 1 + 1) * 1 digits
    # 10-99-> (99 - 10 + 1) * 2 digits
    # 100-199-> (199 - 100 + 1) * 3 digits
    res = 0
    digits = 1
    tenPow = 1
    prevNum = 0
    curNum = 10 ** tenPow - 1
    
    while curNum <= n:
        res += (curNum - prevNum) * digits
        tenPow += 1
        prevNum = curNum
        curNum = 10 ** tenPow - 1
        digits += 1
    return res + (n - prevNum) * digits