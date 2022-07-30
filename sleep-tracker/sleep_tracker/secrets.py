import os

AS_ADDON = True

HOME_ASSISTANT_TOKEN = os.getenv("SUPERVISOR_TOKEN")
CACHE_PATH = "/data/.cache"
FITBIT_CLIENT_ID = ""
FITBIT_CLIENT_SECRET = ""
HOME_ASSISTANT_URL = "http://supervisor/core/api/states/sensor.sleep"


OPTIONS_PATH = "/data/options.json"

import json

with open(OPTIONS_PATH, "r") as fp:
  options = json.load(fp)
  FITBIT_CLIENT_ID = options["fitbit_client_id"]
  FITBIT_CLIENT_SECRET = options["fitbit_client_secret"]
