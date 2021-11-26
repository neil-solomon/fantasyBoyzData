import os
import sys
import json


for dir in ["2018", "2019", "2020"]:
    for (dirpath, dirnames, filenames) in os.walk(f"../data/{dir}/matchups"):
        for filename in filenames:
            if "json" in filename:
                continue
            with open(f"{dirpath}/{filename}", "r") as file:
                print(f"{dirpath}/{filename}")
                matchups = []
                matchups_list = file.read().split("\n")
                for matchup in matchups_list:
                    matchup_list = matchup.split(" ")
                    is_playoff = True if matchup_list[0].split("=")[1] == "t" else False
                    is_postseason = True if matchup_list[1].split("=")[1] == "t" else False
                    is_championship = True if matchup_list[2].split("=")[1] == "t" else False
                    player_1_name = matchup_list[3].split("=")[0]
                    player_1_score = float(matchup_list[3].split("=")[1])
                    player_2_name = matchup_list[4].split("=")[0]
                    if player_2_name == "BYE":
                        player_2_name = None
                        player_2_score = None
                    else:
                        player_2_score = float(matchup_list[4].split("=")[1])

                    matchups.append({
                        "isPostseason": is_postseason,
                        "isPlayoff": is_playoff,
                        "isChampionship": is_championship,
                        "player1Name": player_1_name,
                        "player1Score": player_1_score,
                        "player2Name": player_2_name,
                        "player2Score": player_2_score,
                    })

            new_filename = filename.split(".")[0]
            print(matchups, new_filename)

            with open(f"{dirpath}/{new_filename}.json", "w+") as file:
                json.dump(matchups, file)