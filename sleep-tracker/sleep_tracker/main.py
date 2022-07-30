import asyncio
import requests
import datetime

from dateutil import parser

from sleep_tracker import authentication
from sleep_tracker import secrets


sleep_state_map = {
    "wake": 0,
    "rem": 1,
    "light": 2,
    "deep": 3
}


async def main():

    auth = authentication.Authenticator()
    if not auth.is_client_valid():
        auth.start_server()
        await auth.get_client()
        auth.stop_server()

    while True:
        sleep_data_today = auth.client.sleep(date=datetime.date.today())
        sleep_data_yesterday = auth.client.sleep(date=(datetime.date.today() - datetime.timedelta(days=1)))

        out = [[int(parser.parse(stage["dateTime"]).timestamp() * 1000), sleep_state_map[stage["level"]]] for sleep_data in [sleep_data_yesterday, sleep_data_today] for sleep in sleep_data["sleep"] for stage in sleep["levels"]["data"]]

        headers = {
            "Authorization": "Bearer " + secrets.HOME_ASSISTANT_TOKEN,
            "content-type": "application/json",
        }

        data = {
            "state": sleep_data_today["summary"]["totalMinutesAsleep"],
            "attributes": {
                "history": out
            }
        }

        requests.post(secrets.HOME_ASSISTANT_URL, json=data, headers=headers)
        print("posted.")

        print("sleeping for 60 seconds...")
        await asyncio.sleep(60)




asyncio.run(main())