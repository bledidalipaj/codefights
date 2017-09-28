"""
You guys should probably know the simple y = sin(x) equation.

Given a range of x [start, end], your mission is to calculate the total signed area of the region in the xy-plane that 
is bounded by the sin(x) plot, the x-axis and the vertical lines x = start and x = end. The area above the x-asix should 
be added to the result, and the area below it should be subtracted.

Example

For start = 0 and end = 10, the output should be
sinArea(start, end) = 1.83907.



For start = 4 and end = 6, the output should be
sinArea(start, end) = -1.61381.



Input/Output

[time limit] 4000ms (py)
[input] integer start

Constraints:
-3·106 < start < 3·106

[input] integer end

Constraints:
-3·106 < start ≤ end < 3·106

[output] float

The signed area.

Your answer will be considered correct if its absolute error doesn't exceed 10-5.

# Challenge's link: https://codefights.com/challenge/L7EqDZzBuE5twLtAD #
"""
def sinArea(start, end):
    return math.cos(start) - math.cos(end)