/*
This is a reverse challenge.

Have fun! :)

[time limit] 4000ms (py3)
[input] integer num

Constraints:
1 ≤ num ≤ 109.

Input:
num: 1
Output:
Empty
Expected Output:
0

Input:
num: 5
Output:
Empty
Expected Output:
1

Input:
num: 12
Output:
Empty
Expected Output:
2

Input:
num: 100
Output:
Empty
Expected Output:
24

# Challenge's link: https://codefights.com/challenge/fRHHjzTpn2eN46cN3/solutions/tBabwPYqs3LStaLYQ
*/

int ZeroAtDEnd(int n) {
    return n < 5 ? 0 : ZeroAtDEnd(n /= 5) + n;
}