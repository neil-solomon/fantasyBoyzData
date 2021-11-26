import json

with open("legacyData.json", "r") as file:
    data = json.load(file)

averageScores = [0] * len(data["players"][0]["regularSeasonPoints"])
count = [0] * len(averageScores)

# sum regular season points across all teams for each season
for i in range(len(averageScores)):
    for player in data["players"]:
        if player["regularSeasonPoints"][i] > 0:
            averageScores[i] += player["regularSeasonPoints"][i]
            count[i] += 1

# divide by the number of teams in a season
for i in range(len(averageScores)):
    averageScores[i] /= count[i]

# assume 13 games in a season
for i in range(len(averageScores)):
    averageScores[i] /= 13

data["averageGameScore"] = averageScores

with open("legacyData.json", "w") as file:
    data = json.load(file)
