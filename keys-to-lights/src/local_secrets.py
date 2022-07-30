import os
import json

AS_ADDON = True

CACHE_PATH = "/data/.cache" if AS_ADDON else os.path.join(os.path.dirname(__file__), "..", ".cache")
OPTIONS_PATH = "/data/options.json" if AS_ADDON else os.path.join(os.path.dirname(__file__), "..", "options.json")


with open(OPTIONS_PATH, "r") as fp:
  options = json.load(fp)


HOME_ASSISTANT_TOKEN = os.getenv("SUPERVISOR_TOKEN") if AS_ADDON else options["supervisor_token"]
HOME_ASSISTANT_URL = "http://supervisor/core/api/services/light/turn_on" if AS_ADDON else "https://assistant.samuelbanning.com/api/services/light/turn_on"
SPOTIFY_CLIENT_ID = options["spotify_client_id"]
SPOTIFY_CLIENT_SECRET = options["spotify_client_secret"]