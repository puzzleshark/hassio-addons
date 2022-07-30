import os
import json

AS_ADDON = False

CACHE_PATH = "/data/.cache" if AS_ADDON else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".cache"))
MUSIC_PATH = "/data/music" if AS_ADDON else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "music"))
OPTIONS_PATH = "/data/options.json" if AS_ADDON else os.path.join(os.path.dirname(__file__), "..", "options.json")


with open(OPTIONS_PATH, "r") as fp:
  options = json.load(fp)

SPOTIFY_CLIENT_ID = options["spotify_client_id"]
SPOTIFY_CLIENT_SECRET = options["spotify_client_secret"]
SPOTIFY_PLAYLIST_ID = options["spotify_playlist_id"]