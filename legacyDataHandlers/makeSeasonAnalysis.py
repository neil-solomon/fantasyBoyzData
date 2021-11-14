import json

with open("../data/2013-2017_data.json", "r") as file:
    data = json.load(file)

dataBySeason = {
    2013: [],
    2014: [],
    2015: [],
    2016: [],
    2017: []
}

for i in range(len(dataBySeason)):
    for player in data["players"]:
        if player["regularSeasonPoints"][i] == 0.0:
            continue

        newPlayerData = { "name" : player["name"]}

        for key in player.keys():
            if key == "name" or key == "bigGames":
                continue
            newPlayerData.update({ key : player[key][i] })

        dataBySeason[2013 + i].append(newPlayerData)

for season in dataBySeason:
    with open(f"../data/{season}/seasonStats.json", "w+") as file:
        json.dump(dataBySeason[season], file)