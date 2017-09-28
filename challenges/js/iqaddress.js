/*
Have you ever heard of an IQ-address? For the given integer n, it is calculated as follows:

Let result = "".
If n = 1, prepend "1" to the beginning of result and return it as an answer.
Prepend n % 10.5 to the beginning of result.
Divide n by 2 with rounding up to the nearest integer.
Go to step 2.
Given an integer n, your task is to return IQ-address generated from it.

Example

For n = 21, the output should be
iqAddress(n) = "12.03.06.00.50.0".

Here's why:

21% 10.5 = 0.0
11% 10.5 = 0.5
6 % 10.5 = 6.0
3 % 10.5 = 3.0
2 % 10.5 = 2.0
Thus, the answer is "1"+"2.0"+"3.0"+"6.0"+"0.5"+"0.0" = "12.03.06.00.50.0".

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 105.

[output] string

The IQ-address generated from n.

# Challenge's link: https://codefights.com/challenge/Y7C33HX5SWeb8vEKd #

toFixed() returns a string, with the number written with a specified number of decimals:

var x = 9.656;
x.toFixed(0);           // returns 10
x.toFixed(2);           // returns 9.66
x.toFixed(4);           // returns 9.6560
x.toFixed(6);           // returns 9.656000

toPrecision() returns a string, with a number written with a specified length:

var x = 9.656;
x.toPrecision();        // returns 9.656
x.toPrecision(2);       // returns 9.7
x.toPrecision(4);       // returns 9.656
x.toPrecision(6);       // returns 9.65600

 */
function iqAddress(n) {
    if (n == 1) {
        return "1";
    }
    return iqAddress(Math.ceil(n / 2)) + (n % 10.5).toFixed(1);
}