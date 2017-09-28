/*
Consider a slider that has several integer points sorted in ascending order. A user can drag the control (a button) to a specific point to choose the desired value.

If the control is dropped between the points, it should automatically move to the value that is immediately before or after its current position. The control should move all the way towards the next value if it has covered at least threshold distance to it from the previous integer point, or jump back to the previous integer if the covered distance is less than the threshold.

Given the lastPoint of the control that allows you to determine its direction, the value of the threshold and the final inputPosition of the control, return the point on the slider that the control should jump to.

Example

For lastPoint = 5, threshold = 0.3 and inputPosition = 2.4,
the output should be
FindClosestPointWithInclination(lastPoint, threshold, inputPosition) = 2.

The control was dragged to the left and has covered the distance from 3 to 2 equal to 0.6, which is greater than 0.3. Thus, it should move all the way to 2.

Input/Output

[time limit] 4000ms (js)
[input] integer lastPoint

Currently selected point.

Constraints:
1 ≤ lastPoint ≤ 10.

[input] float threshold

The threshold.

Constraints:
0.03 ≤ threshold ≤ 0.97.

[input] float inputPosition

The position at which the control was dropped.

Constraints:
0 ≤ inputPosition ≤ 10.

[output] integer

The point to which the control should move.

# Challenge's link: https://codefights.com/challenge/28tEZBaS4BsjJXjWv #

 */
function FindClosestPointWithInclination(lastPoint, threshold, inputPosition) {
    // had to add 0.0001 becuase 4 - 3.7 = 0.2999999999999998
    if (inputPosition - lastPoint > 0) {
        if (inputPosition - parseInt(inputPosition) + 0.0001>= threshold) {
            inputPosition = Math.ceil(inputPosition);
        } else {
            inputPosition = Math.floor(inputPosition);
        }
    } else {
        if (Math.ceil(inputPosition) - inputPosition + 0.0001 >= threshold) {
            inputPosition = Math.floor(inputPosition);
        } else {
            inputPosition = Math.ceil(inputPosition);
        }
    }
    return inputPosition;
}