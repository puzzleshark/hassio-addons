import os

AS_ADDON = True

HOME_ASSISTANT_TOKEN = os.getenv("SUPERVISOR_TOKEN")
CACHE_PATH = "/data/.cache"
FITBIT_CLIENT_ID = ""
FITBIT_CLIENT_SECRET = ""
HOME_ASSISTANT_URL = "http://supervisor/core/api/states/sensor.sleep"