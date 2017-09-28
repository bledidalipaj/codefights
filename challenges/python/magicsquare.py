"""
An n × n magic square is a square containing n2 numbers such that the sum of the numbers in every row, column, and diagonal is the same.

For instance, here's an example of a 3 × 3 magic square:

4  9  2
3  5  7
8  1  6
The sum of every row, column, and diagonal is exactly 15. This is called the "Lo Shu" magic square, and it can be 
represented by the following matrix:

[[4,9,2],
 [3,5,7],
 [8,1,6]]
Given integers start, step and n, your task is to return a matrix of size n × n representing a magic square. The matrix 
should be filled with numbers start, start + step, start + 2 * step, ...,, and among all possible answers be lexicographically 
smallest.

If there is no answer, return empty array instead.

Example

For start = 1, step = 1 and n = 3, the output should be

magicSquare(start, step, n) = [[2, 7, 6], 
                               [9, 5, 1], 
                               [4, 3, 8]]
Input/Output

[time limit] 4000ms (py)
[input] integer start

The smallest number in the magic square.

Constraints:

-3000 ≤ start ≤ 3000.

[input] integer step

The difference between each pair of subsequent numbers in the magic square.

Constraints:

1 ≤ step ≤ 100.

[input] integer n

The size of the square;

Constraints:

1 ≤ n ≤ 4.

[output] array.array.integer

The lexicographically smallest magic square made of the first n2 integers of the sequence start, start + step, start + 2 * step, 
..., or [] if no such square exists.

# Challenge's link: https://codefights.com/challenge/MSrdnNFJJsgxkLyEr/solutions/cEzikLWBs38bkC9TX #
"""
def magicSquare(start, step, n):
    if n == 1:
        return [[start]]
    if n == 2:
        return []
    if n == 3:
        return [
            [start + 1*step, start + 6*step, start + 5*step],
            [start + 8*step, start + 4*step, start + 0*step],
            [start + 3*step, start + 2*step, start + 7*step]
        ]
    if n == 4:
        return [
            [ start + 0*step, start + 1*step, start + 14*step, start + 15*step],
            [ start + 11*step, start + 13*step, start + 2*step, start + 4*step],
            [ start + 12*step, start + 6*step, start + 9*step, start + 3*step],
            [ start + 7*step, start + 10*step, start + 5*step, start + 8*step]
        ]