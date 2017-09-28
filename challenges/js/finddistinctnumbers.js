/*
Given an array a, your task is to find the distinct numbers in it and return them in the order
 that they appear in a. The input array might contain duplicate numbers, while the resulting 
 array should contain only one instance of each number.

Example

For a = [8, 4, 8, 4, 20], the output should be
findDistinctNumbers(a) = [8, 4, 20].

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

An array of integers.

Constraints:
0 ≤ a.length ≤ 8000,
-109 ≤ a[i] ≤ 109.

[output] array.integer

An array containing the distinct integers of the given array in the order in which they appear.

# Challenge's link: https://codefights.com/challenge/rWc6njYjh34HBzzPJ/ #
 */
findDistinctNumbers = a => [...new Set(a)]

function findDistinctNumbers(a) {
    var mySet = new Set(a);
    var result = [];
    for(var item of mySet) {
        result.push(item);
    }
    return result;
}