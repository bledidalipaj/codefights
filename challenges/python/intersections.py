"""
You are given an array of lines. Each line is expressed as an array [m, b], which stands for the line defined by the equation y = m * x + b.

You are also given an array of circles. Each circle is expressed as an array [h, k, r], which represents the circle defined by the equation 
(x - h)2 + (y - k)2 = r2.

Let l_max be the maximum number of circles that a given line intersects. Let c_max be the maximum number of lines that intersect a given circle.

Of all possible values of l_max and c_max, return the largest one.

Example

For lines = [[1, 0], [-1, 0], [0, -2]] and
circles=[[0, 0, 1], [2, 2, 1], [4, 4, 1]],
the output should be
Intersections(lines, circles) = 3.

Line [1,0] intersects all three circles, while each circle is intersected by at most two lines.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer lines

Array of lines, where each line is given as described above.

Constraints: 
2 ≤ lines.length ≤ 50,
lines[i].length = 2,
-100 ≤ lines[i][0], lines[i][1] ≤ 100.

[input] array.array.integer circles

Array of circles, each element of circles represents a circle as described above.

Constraints: 
2 ≤ circles.length ≤ 50,
circles[i].length = 3,
-100 ≤ circles[i][0], circles[i][1] ≤ 100,
1 ≤ circles[i][2] ≤ 100.

[output] integer

The maximum of all possible l_max and c_max.

# Challenge's link: https://codefights.com/challenge/EdNcNqGNwddzctaoe/main #
"""
def Intersections(lines, circles):
    
    line_inters_circles = [0] * len(lines)
    circle_inters_lines = [0] * len(circles)
    
    def intersect(line_params, circle_params):
        m, b = line_params
        h, k, r = circle_params
        x1, y1 = 0 - h, b - k
        x2, y2 = 1 - h, m + b - k
        D = x1*y2 - x2*y1
        discr = ((x1 - x2) ** 2 + (y1 - y2) ** 2) * r ** 2 - D ** 2
        return discr >= 0
    
    for line_index in xrange(len(lines)):
        for circle_index in xrange(len(circles)):
            if intersect(lines[line_index], circles[circle_index]):
                line_inters_circles[line_index] += 1
                circle_inters_lines[circle_index] += 1
                
    return max( max(line_inters_circles),
                max(circle_inters_lines) )