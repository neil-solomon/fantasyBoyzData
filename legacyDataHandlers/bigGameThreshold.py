with open("data/2013-2017_200PointGames.txt", "r") as file:
    games = file.read().split("\n")

gamesBySeason = [[], [], [], [], []]

for game in games:
    year = int(game.split("-")[1].split(",")[0].split(" ")[2])
    score = float(game.split("-")[0].split(" ")[0])
    gamesBySeason[year-2013].append(score)

for season in gamesBySeason:
    season.sort()

averageScores = [
    144.02197802197801,
    149.69230769230768,
    144.90865384615384,
    136.83846153846156,
    147.96221153846153
]

for i in range(len(gamesBySeason)):
    print(gamesBySeason[i][0] / averageScores[i])
