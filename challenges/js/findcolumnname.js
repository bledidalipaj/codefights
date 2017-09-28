/*
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
 */
function FindColumnName(col) {
    var colName = '';
    
    while (col > 0) {
        var m = col % 26;
        
        if (m == 0) {
            m = 26;
            col -= 1;
        }
        var char = String.fromCharCode(64 + m);
        colName = char + colName;
        col = Math.floor(col / 26);
    }
    return colName;
}