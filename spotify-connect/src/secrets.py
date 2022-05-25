import os

AS_ADDON = True

HOME_ASSISTANT_TOKEN = os.getenv("SUPERVISOR_TOKEN")
CACHE_PATH = "/data/.cache"
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
HOME_ASSISTANT_URL = "http://supervisor/core/api/services/light/turn_on"


OPTIONS_PATH = "/data/options.json"

import json

with open(OPTIONS_PATH, "r") as fp:
  options = json.load(fp)
  SPOTIFY_CLIENT_ID = options["spotify_client_id"]
  SPOTIFY_CLIENT_SECRET = options["spotify_client_secret"]