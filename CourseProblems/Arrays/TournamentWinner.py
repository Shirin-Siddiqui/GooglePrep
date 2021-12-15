
'''
PROBLEM STATEMENT - TOURNAMENT WINNER
'''

# O(n) - Time Complexity where n is the number of competitions
# O(k) - Space Complexity where k is the number of teams
def tournamentWinner(competitions, results):
    scores = {}
    i = 0
    for number in results:
        if competitions[i][0] not in scores:
            scores[competitons[i][0]] = 0
        if competitons[i][1] not in scores:
            scores[competitons[i][1]] = 0

        if number == 0:
            scores[competitions[i][1]] += 3
        else:
            scores[competitions[i][0]] += 3
        i += 1
    return max(zip(scores.values(), scores.keys()))[1]

competitons = [
    ["HTML","C#"],
    ["C#","Python"],
    ["Python", "HTML"]
]
results = [0,0,1]

print(tournamentWinner(competitons, results))
			