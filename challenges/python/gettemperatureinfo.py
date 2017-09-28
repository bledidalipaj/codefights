"""
Your area of research is climate change, and you collect the temperatures on consecutive days during a certain 
period of time. Now you want to find out how the average temperature changed over that time span, so you need to 
find the average temperature after each new measurement. You don't think that digits after the decimal point make 
any difference, so you calculate rounded average temperatures. To make the process more entertaining, you round the 
first value up, the second one down, the third one up, and so on.

In other words, the results array should contain the following values: [ceil(t[0] / 1), floor((t[0] + t[1]) / 2), 
ceil((t[0] + t[1] + t[2]) / 3), ...]. Here t is used as shorthand for measurements, ceil means round up to the nearest 
integer value, and floor means round down.

Given a list of measurements, return the average temperatures after each measurement has been rounded as described above.

Example

For measurements = [12, -5, 9], the output should be
getTemperatureInfo(measurements) = [12, 3, 6].

The first value in the results array remains the same, 12, since the average of one value is just itself. The second value 
in the results array is the average of 12 and -5, rounded down. The third value in the results array is the average of 12, -5, 
and 9, rounded up.

[time limit] 4000ms (py)
[input] array.integer measurements

Temperature values for consecutive measurements.

Constraints:
1 ≤ measurements.length ≤ 20,
-50 ≤ measurements[i] ≤ 50.

[output] array.integer

# Challenge's link: https://codefights.com/challenge/uJgCw8pfLQoLhTyMM #
"""
def getTemperatureInfo(measurements):
    res = []
    curSum = 0
    for i in range(len(measurements)):
        curSum += measurements[i]
        if i % 2 == 0:
            avg = math.ceil(curSum * 1.0 / (i + 1))
        else:
            avg = curSum / (i + 1)
        res.append(avg)
    return res