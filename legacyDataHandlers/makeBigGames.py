import json

with open("data/2013-2017_200PointGames.txt", "r") as file:
    games = file.read().split("\n")

avgScores = [
    144.02197802197801,
    149.69230769230768,
    144.90865384615384,
    136.83846153846156,
    147.96221153846153
]

bigGamesBySeason = {}

for game in games:
    player = game.split("-")[1].split(" ")[1]
    year = int(game.split("-")[1].split(",")[0].split(" ")[2])
    try:
        week = int(game.split("week")[1])
    except:
        continue
    score = float(game.split("-")[0].split(" ")[0])

    if year not in bigGamesBySeason:
        bigGamesBySeason[year] = []
    
    bigGamesBySeason[year].append({
        "player": player,
        "week": week,
        "score": score,
        "pctAboveAvg": score / avgScores[year-2013] * 100 - 100
    })

for season in bigGamesBySeason:
    with open(f"data/{season}/bigGames.json", "w+") as file:
        json.dump(bigGamesBySeason[season], file)
