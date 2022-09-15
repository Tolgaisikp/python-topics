import requests

key = "c701fd768a7e4195855ea317a60f1641"
query = "god of war"

r = requests.get(f'https://api.rawg.io/api/games?key={key}&search={query}')


jsonData = r.json()
print("count of search:", jsonData["count"])
games = jsonData["results"]

for idx, game in enumerate(games):
   if idx > 5:
       print(game['name'], "\n", game['background_image'], "\n", game["id"])
