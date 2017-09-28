"""
You are given a 2D matrix. Every diagonal in the matrix, including the main diagonal that runs from its top left 
corner to its bottom right corner and all of the diagonals running parallel to it, must be composed of same element. 
Each diagonal can contain a different element. A matrix is considered good if each of its diagonals meets these 
requirements.

Example

For matrix = [
  [7, 3, 5, 1],
  [5, 7, 3, 5], 
  [1, 5, 7, 3],
  [2, 1, 5, 7]
], the output should be
isGoodMatrix(matrix) = true.
Let's collect numbers in each diagonal:

1
5 5
3 3 3
7 7 7 7
5 5 5
1 1
2
Each diagonal is composed of the same number, meaning that the matrix is good and the answer is true.

For matrix = [
  [1, 2, 3, 4],
  [0, 1, 4, 3], 
  [4, 0, 2, 2],
  [4, 2, 0, 1]
], the output should be
isGoodMatrix(matrix) = false.
There are three diagonals in which every cell does not have the same element:

2 4 2
1 1 2 1
4 2
The matrix is not good and the answer is false.

[time limit] 4000ms (py3)
[input] array.array.integer matrix

1 ≤ matrix.length ≤ 10
matrix[i].length = matrix.length
-100 ≤ matrix[i][j] ≤ 100

[output] boolean

# Challenge's link: https://codefights.com/challenge/teS5pB7RPT6kJchgW #
"""
def isGoodMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for x in range(rows):
        i = x
        j = 0
        diagonal1Elem = matrix[i][j]
        diagonal2Elem = matrix[j][i]
        while i < rows and j < cols:
            if curElem1 != matrix[i][j] or curElem2 != matrix[j][i]:
                return False
            i += 1
            j += 1
    return True