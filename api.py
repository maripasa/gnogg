import requests
import json

def get_steam_games(api_key, id):
    steam_url = (
        "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        f"?key={api_key}&steamid={id}&include_appinfo=1&format=json"
    )
    steam_games = []

    response = requests.get(steam_url)
    response.raise_for_status()
    data = response.json()
    games = data.get("response", {}).get("games", [])
    steam_games = [game["name"] for game in games if "name" in game]

    return steam_games
