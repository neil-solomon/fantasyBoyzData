import json

with open("legacyData.csv", "r") as file:
    rows = file.readlines()

players = {}
rowCount = 0

for row in rows:
    cols = row.split(",")

    if cols[0] == "":
        continue

    if rowCount == 0:
        playerKey = cols[0]
        players[playerKey] = {}
    else:
        players[playerKey][cols[0]] = [
            float(val.strip("\n"))
            if val.strip("\n") != "" else 0.0
            for val in cols[1:]
        ]
        
    rowCount += 1
    if rowCount == 8:
        rowCount = 0

with open("legacyData.json", "w+") as file:
    file.write(json.dumps(players))
