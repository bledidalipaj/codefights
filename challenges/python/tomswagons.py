"""
Tom goes to a train station every afternoon to watch the 2pm train go. He has noted that the number of wagons the train has 
is always an odd number, and that every day the number of wagons the train has increases by 2, starting with 1 wagon on the 
first day of each month.

Thus, on the 1st day of each month the train goes with a single wagon, on the 2nd day it has 3 wagons, the next day it has 5 
wagons, and so on.

The routine of counting the wagons comforts Tom, and he never misses a day. But on the dayth day of a certain month he will 
have to go to a camp that will last for n days. During these days, Tom will not be able to come and count the wagons.

Given the day, the month and the number n, your task is to calculate the number of wagons Tom will miss. Assume that this and 
the following years are both non-leap.

Example

For month = 1, day = 1 and n = 1, the output should be
toms_wagons(month, day, n) = 1.

Tom will miss only the train that leaves on the first of January. This train will have only one wagon, so the answer is 1.

For month = 3, day = 2 and n = 4, the output should be
toms_wagons(month, day, n) = 24.

Tom will miss 4 March days, from the 2nd to the 5th. Thus, he will miss 3 + 5 + 7 + 9 = 24 wagons.

Input/Output

[time limit] 4000ms (py)
[input] integer month

The 1-based month of the year.

Constraints:
1 ≤ month ≤ 12.

[input] integer day

The day of the month when the camp starts.

Constraints:
1 ≤ day ≤ the_number_of_days_in_the_ith_ month.

[input] integer n

The number of days Tom will spend in the camp (equal to the number of trains he will miss).

Constraints:
0 ≤ n ≤ 365.

[output] integer

The number of wagons Tom will miss.

# Challenge's link: https://codefights.com/challenge/X8dWNNGxbAAnMkBaB #
"""
def toms_wagons(month, day, n):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    missedWagons = 0
    numOfWagons = 1 + (day - 1) * 2
    curDay = day
    daysMissed = 0
    
    while daysMissed < n:
        if curDay > daysInMonth[month - 1]:
            curDay = 1
            numOfWagons = 1
            month += 1
        if month > 12:
            month = 1
        
        missedWagons += numOfWagons 
        curDay += 1
        numOfWagons += 2
        daysMissed += 1
    return missedWagons