"""
You would like to create your own little farm. Since you're not an expert (yet!), you bought seeds of just two types of plants: 
flowers and florets. Each pack of seeds was provided with the instructions, explaining when the plant can be planted.

In the instructions two dates are given, to and from, which denote the favorable period for planing the seeds. Note, that to is 
not necessarily larger than from: if to is less than from, then the period is counted from to to from through the beginning of 
the new year. It is always assumed that there are 365 days in a year.

Given the dates from the flower instructions flowerFrom and flowerTo and from the floret instructions floretFrom and floretTo, 
calculate the number of days of the year in which both plants can be planted.

Example

For flowerFrom = 10, flowerTo = 20,
floretFrom = 1 and floretTo = 365, the output should be
flowersAndFlorets(flowerFrom, flowerTo, floretFrom, floretTo) = 11.

Flowers can only be planted in the period from the 10th to the 20th day of the year, and florets can be planted any time. Thus, 
the output should be equal to the number of days in which flowers can be planted, which is 11.

For flowerFrom = 100, flowerTo = 150,
floretFrom = 110 and floretTo = 130, the output should be
flowersAndFlorets(flowerFrom, flowerTo, floretFrom, floretTo) = 21.

The favorable days for planting overlap in the period from the 110th to the 130th day of the year, 21 days in total.

For flowerFrom = 360, flowerTo = 10,
floretFrom = 1 and floretTo = 365, the output should be
flowersAndFlorets(flowerFrom, flowerTo, floretFrom, floretTo) = 16.

Flowers can only be planted in the period from the 1th to the 10th day of the year, and from the 360th to the 365th days, and 
florets can be planted any time. Thus, the output should be equal to the number of days in which flowers can be planted, which is 16.

Input/Ouptut

[time limit] 4000ms (py)
[input] integer flowerFrom

The starting day of flowers planting season.

Constraints:
1 ≤ flowerFrom ≤ 365.

[input] integer flowerTo

The last day of flowers planting season.

Constraints:
1 ≤ flowerTo ≤ 365,
flowerTo ≠ flowerFrom.

[input] integer floretFrom

The starting day of florets planting season.

Constraints:
1 ≤ floretFrom ≤ 365.

[input] integer floretTo

The last day of florets planting season.

Constraints:
1 ≤ floretTo ≤ 365,
floretTo ≠ floretFrom.

[output] integer

The number of days in which both type of seeds can be planted.

# Challenge's link: https://codefights.com/challenge/Qk4DePWLz72jnfsXy #
"""
def flowersAndFlorets(flowerFrom, flowerTo, floretFrom, floretTo):
    def favorableDays(fromDay, toDay):
        days = set()
        day = fromDay
        
        while day != toDay:
            days.add(day)
            day += 1
            
            if day > 365:
                day = 1
        days.add(toDay)
        return days
    
    flowerFavorableDays = favorableDays(flowerFrom, flowerTo)
    floretFavorableDays = favorableDays(floretFrom, floretTo)
    commonDays = flowerFavorableDays.intersection(floretFavorableDays)
    return len(commonDays)

def flowersAndFlorets(flowerFrom, flowerTo, floretFrom, floretTo):
    def getFineDates(fr, to):
        res = [False] * 365
        if to > fr:
            res[fr - 1 : to] = [True] * (to - fr + 1)
        else:
            res[:to] = [True] * to
            res[fr - 1:] = [True] * (365 - fr + 1)
        return res

    res1 = getFineDates(flowerFrom, flowerTo)
    res2 = getFineDates(floretFrom, floretTo)
    return len([1 for i in range(365) if res1[i] and res2[i]])