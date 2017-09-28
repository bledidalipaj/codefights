"""
This is a reverse challenge, enjoy!

[time limit] 4000ms (py3)
[input] integer Col

Constraints:
1 ≤ Col ≤ 2 · 109.

[output] string

Input:
Col: 100
Output:
Empty
Expected Output:
"CV"

Input:
Col: 10001
Output:
Empty
Expected Output:
"NTQ"

Input:
Col: 99000
Output:
Empty
Expected Output:
"EPKR"
"""
def FindColumnName(col):
    colName = []
    
    while col > 0:
        m = col % 26
        if m == 0:
            letter = 'Z'
            col -= 1
        else:
            letter = chr(64 + m)
        colName.append(letter)
        
        col //= 26 
    return ''.join(colName)[::-1]