"""
There are one hundred residents in Smalltown, and ten of them make up the mafia. The newly assigned 
Commissioner wants to find all members of the mob. To do this, he demanded every resident to compile 
a list of ten suspects from the remaining 99 residents.

None of the mafia mentioned the other mobsters, but every civilian has included in their list at least 
seven mafiosi. To ensure the safety of the residents and prevent the vengeance, the Commissioner 
assigned every dweller an identification number (0-based) and has replaced all the names by these id 
numbers. Now he needs your help to reveal all the Mafia by analyzing the residents' answers.

Given a list of answers, return a list of 10 mafiosi sorted in ascending order.

Example

Let the residents with identification numbers 0-9 have compiled the same lists [10,11,12,13,14,15,16,17,18,19], 
and let the lists of all the other residents be [0,1,2,3,4,5,6,7,8,9].

The output should then be
Mafia(answers) = [0,1,2,3,4,5,6,7,8,9].

Input/Output

[time limit] 4000ms (py3)
[input] array.array.integer answers

Lists of suspects provided by the residents. The nth row contains the list compiled by the resident with id n.

Constraints:
answers.length = 100,
answers[i].length = 10,
i ∉ answers[i].

[output] array.integer

A sorted list of mafia ids.

# Challenge's link: https://codefights.com/challenge/9MGJonqLaLGREtAnW/solutions/TBBYhRSdE8Fjb5fBo #
"""
def Mafia(answers):
	pass


def Mafia(answers):
    score = [0]* 100
    for i in range(100):
        for j in range(i+1, 100):
            if len(set(answers[i]) & set(answers[j])) >= 4:
                score[i] += 1
                score[j] += 1
    mafia = sorted([[j, i] for i, j in enumerate(score)])[0:10]
    mafia = [i[1] for i in mafia]
    return sorted(mafia)

def Mafia(answers):
    mafias = []
    mcounts = [0] * 100
    for i in answers:
        for j in i:
            mcounts[j] = mcounts[j] + 1
    
    X = {}
    for i,j in enumerate(mcounts):
        if j > 10:
            mafias.append(i)
            X[i] = j
    
    s = sorted(mafias)[::-1]
    
    rems = []
    new_s = []
    for i,j in enumerate(s):
        nums = answers[j]
        c = 0
        for n in nums:
            if n in X:
                if X[n] > 50:
                    c += 1
        if c < 4:
            new_s.append(j)
    
    
    new_idx = [i for i in new_s]
    for i,j in enumerate(answers):
        c = 0
        for k in j:
            if k in new_idx:
                c += 1
        if c == 0 and i not in new_s:
            print i,c,j
            new_s.append(i)
                
    r = []
    for i in range(min(10,len(new_s))):
        r.append(new_s[i])
    
    return sorted(r)

def Mafia(y):
    z = []
    for i,a in enumerate(y):
        x = 1
        if z:
            for c in z:
                if len(set(a).intersection(set(c[0][1]))) > 3 and x:
                    c.append([i,a])
                    x = 0
        if x:
            z.append([[i,a]])
    o = []
    for c in z:
        if len(c) < 11:
            for i in c:
                o.append(i[0])
    return sorted(o)


from collections import Counter
def Mafia(a):
    c = Counter()
    for s in a: c.update(s)
    g = {}
    i = 0
    for s in a:
        for r in s:
            g.setdefault(i, 0)
            g[i] += c[r]
        i += 1
    return sorted([k for k,v in sorted(g.items(), key=lambda t:t[1])[:10]])