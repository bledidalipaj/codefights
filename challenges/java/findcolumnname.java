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
String FindColumnName(int col) {
    String colName = "";
    
    while (col > 0) {
        int m = col % 26;
        if (m == 0) {
            col -= 1;
            m = 26;
        }
        colName = (char)(m + 64) + colName;
        col /= 26;
    }
    return colName;
}