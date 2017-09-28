/*
You're given an array of unsorted integers arr. Find the maximum length of a contiguous subarray that contains at most 2 different 
integers (possibly several times).

Example

For arr = [7, 4, 5, 4, 4, 6], the output should be
findBiSlice(arr) = 4.

The longest contiguous subarray that consists of only 2 integers is [4, 5, 4, 4], and it contains 4 elements.

Input/Output

[time limit] 4000ms (js)
[input] array.integer arr

Array of integers.

Constraints:
2 ≤ arr.length ≤ 8000,
1 ≤ arr[i] ≤ 104.

[output] integer

The length of the maximal contiguous subarray containing no more than 2 integers.
*/

function findBiSlice(arr) {
    var ans = 0;
    var ln = arr.length;
    
    for(var i = 0; i < ln; i++){
        sub = new Set();
        sub.add(arr[i]);
        var counter = 1;
        
        for(var j = i + 1; j < ln; j++){
            sub.add(arr[j])
            
            if(sub.size <= 2){
                counter++;
            }
            else{
                break;
            }
            ans = Math.max(ans, counter);
            
        }
    }
    return ans;
}