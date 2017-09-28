"""
At the county fair there is a contest to guess how many jelly beans are in a jar. Each entrant is allowed to submit a 
single guess, and cash prizes are awarded to the entrant(s) who come closest without going over. In the event that there 
are fewer guesses less than or equal to the answer than the number of prizes being awarded, the remaining prizes will be 
awarded to the remaining entrants who are closest to the correct answer (however, if there are more prizes than entries, 
the excess prizes will not be awarded). If two or more entrants tie for a finishing position, they will evenly split the 
sum of the prizes for the range of positions they occupy.

Given an array representing the prizes paid for each finishing position, an array of the guesses, and the correct answer, 
return an array of the prizes awarded to each entrant. If a tie results in a fractional prize amount, round up to the nearest 
penny (e.g. $10 / 3 = $3.34).

Example

For prizes = [ [1,1,100], [2,2,50], [3,4,25] ], guesses = [65, 70, 78, 65, 72]
and answer = 70, the output should be
awardedPrizes(prizes, guesses, answer = [37.5, 100.0, 0.0, 37.5, 25.0].

The prizes represent the following prize structure:

1st place wins $100;
2nd place wins $50;
3rd place wins $25;
4th place wins $25.
The entrant who guessed 70 was closest, and wins $100 for 1st place.
The two entrants who guessed 65 were next closest (without going over), and so they split the total prizes for 2nd and 3rd place. 
Thus each wins (50 + 25) / 2 = $37.50.
No one else submitted a guess less than the answer, so the entrant who guessed 72 was next closest, and wins $25 for 4th place.
The entrant who guessed 78 does not win a prize.

The answer is thus [37.5, 100.0, 0.0, 37.5, 25.0].

Input/Output

[time limit] 4000ms (py3)
[input] array.array.integer prizes

An array of prize tiers; each tier is an array with three elements: start_position, end_position, and prize_amount.

The tiers are not necessarily provided in order. However, it is guaranteed that these tiers combine such that there is a single prize 
for each finishing position from 1 through some position k, and no prizes beyond that point (i.e. no gaps in the prize structure).

Constraints:
1 ≤ prizes.length ≤ 20,
1 ≤ prizes[i][0] ≤ prizes[i][1] ≤ 20,
1 ≤ prizes[i][2] ≤ 100.

[input] array.integer guesses

An array of the guesses made by each entrant in the contest.

Constraints:
1 ≤ guesses.length ≤ 100.

[input] integer answer

The actual number of jelly beans in the jar.

Constraints:
1 ≤ answer ≤ 100.

[output] array.float

An array containing the prize awarded to each entrant, in the same order as their guesses.

# Challenge's link: https://codefights.com/challenge/FQJuF4Tsz632pcWgX #
"""
from collections import defaultdict
def awardedPrizes(prizes, guesses, answer):
    res = [0] * len(guesses)
    # sort prizes 
    prizes.sort(key=lambda el: el[0])
    
    # key: answer - entrant guess
    # value: a list which holds the indexes of all the entrants
    # that guessed the same number
    performanceIndexesDict = defaultdict(list)
    for index, guess in enumerate(guesses):
        dist = answer - guess 
        if dist < 0:
            dist = guess 
        performanceIndexesDict[dist].append(index) 
    
    positionPrizeDict = {}
    for prize in prizes:
        for i in range(prize[0], prize[1] + 1):
            positionPrizeDict[i] = prize[2]

    numOfPrizes = len(positionPrizeDict)
    position = 1
    for closestGuess in sorted(performanceIndexesDict.keys()):
        if position > numOfPrizes:
            break 
        winners = performanceIndexesDict[closestGuess]
        cash = 0
        
        for i in range(position, position + len(winners)):
            if i > numOfPrizes:
                break
            cash += positionPrizeDict[i]
        position += len(winners)
        
        # split the total prizes 
        cash /= len(winners)
        
        # round up to the second decimal position
        cash = math.ceil(cash * 100) / 100
        
        for winner in winners:
            res[winner] = cash 
    return res


def awardedPrizes(prizes, guesses, answer):
    res = [0] * len(guesses)

    rewards = [0] * 20
    for start, end, val in prizes:
        for i in range(start - 1, end):
            rewards[i] = val

    sorted_guesses = list(enumerate(guesses))
    sorted_guesses.sort(key=lambda x: (x[1] > answer, abs(x[1] - answer)))

    i = 0
    while i < len(sorted_guesses):
        val = sorted_guesses[i][1]
        cnt = guesses.count(val)
        reward = math.ceil(sum(rewards[i:i + cnt]) / cnt * 100) / 100
        for j in range(i, i + cnt):
            res[sorted_guesses[j][0]] = reward
        i += cnt
    return res