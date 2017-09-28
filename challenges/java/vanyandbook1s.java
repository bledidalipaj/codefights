/*
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
 */
int VanyaAndBook1s(int n) {
    int res = 0,
        digits = 1;
    double tenPow = 1.0,
        prevNum = 0.0,
        curNum = Math.pow(10, tenPow) - 1;
        
    while (curNum <= n) {
        res += (int)(curNum - prevNum) * digits;
        tenPow++;
        prevNum = curNum;
        curNum = Math.pow(10, tenPow) - 1;
        digits++;
    }
    
    return res + (int)((n - prevNum) * digits);
}