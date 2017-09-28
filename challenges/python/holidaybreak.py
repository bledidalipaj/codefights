"""
My kids very fond of winter breaks, and are curious about the length of their holidays including all the weekends.

Each year the last day of study is usually December 22nd, and the first school day is January 2nd (which means that 
the break lasts from December 23rd to January 1st). With additional weekends at the beginning or at the end of the 
break (Saturdays and Sundays), this holiday can become quite long.

The government issued two rules regarding the holidays:

The kids' school week can't have less than 3 studying days. The holidays should thus be prolonged if the number of 
days the kids have to study before or after the break is too little.
If January 1st turns out to fall on Sunday, the following day (January 2nd) should also be a holiday.
Given the year, determine the number of days the kids will be on holidays taking into account all the rules and weekends.

Example

For year = 2016, the output should be
holidayBreak(year) = 11.

First day of the break: Friday December 23rd.
Last day of the break: Monday January 2nd.
Break length: 11 days.

For year = 2019, the output should be
holidayBreak(year) = 16.

First day of the break: Saturday December 21st.
Last day of the break: Sunday January 5th.
Break length: 16 days.

*** Due to complaints, I've added a hidden Test outside of the range. The Year now goes to 2199 ***

[time limit] 4000ms (py)
[input] integer year

The year the break begins.

Constraints:
2016 ≤ year ≤ 2199.

[output] integer

The number of days in the break.

# Challenge's link: https://codefights.com/challenge/yBwcdkwQm5tAG2MJo #
"""
import calendar

def holidayBreak(year):
    first_day = 23
    last_day = 31 + 1

    # first day of the break
    weekday = calendar.weekday(year, 12, 23)
    if weekday == 0:
        first_day -= 2
    elif weekday == 1:
        first_day -= 3
    elif weekday == 2:
        first_day -= 4
    elif weekday == 6:
        first_day -= 1

    # last day of the break
    weekday = calendar.weekday(year + 1, 1, 1)
    if weekday == 6 or weekday == 5:
        last_day += 1
    elif weekday == 4:
        last_day += 2
    elif weekday == 3:
        last_day += 3
    elif weekday == 2:
        last_day += 4
    return last_day - first_day + 1