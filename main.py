import requests
import pprint

api_key = "qxwn52dqxvaqkfuf9z2fsfbb"
season_year = "2021"
season_phase = "REG"

# Get the list of games in the season
games_url = f"https://api.sportradar.us/nba/trial/v8/en/games/2021/REG/schedule.json?api_key={api_key}"
games_response = requests.get(games_url)
games_data = games_response.json()

# Loop through each game and retrieve the extended box score
count = 0
for game in games_data["games"]:
    game_id = game["id"]
    try:

        boxscore_url = f"https://api.sportradar.us/nba/trial/v8/en/games/{game_id}/summary.json?api_key={api_key}"
        boxscore_response = requests.get(boxscore_url)
        boxscore_data = boxscore_response.json()
    except:
        boxscore_data = "null no data this time"
    count += 1
    if count > 3:
        break
    # Do something with the boxscore_data, such as
    pprint.pprint(boxscore_data)
    f = open("demofile2.txt", "a")
    f.write(pprint.pformat(boxscore_data))
    f.close()