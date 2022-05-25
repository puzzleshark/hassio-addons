import asyncio
import fitbit
import json
import os

from quart import Quart, request

import secrets


def load_token_dict():
    if not os.path.isfile(secrets.CACHE_PATH):
        pass
    with open(secrets.CACHE_PATH, "r") as fp:
        token_dict = json.load(fp)
        return token_dict


def save_token_dict(token_dict):
    with open(secrets.CACHE_PATH, "w") as fp:
        json.dump({
            "access_token": token_dict["access_token"],
            "refresh_token": token_dict["refresh_token"],
            "expires_at": token_dict["expires_at"]
        }, fp)


class Authenticator:

    def __init__(self):
        self.server = None
        self.app = None
        self.event = asyncio.Event()

        if not os.path.isfile(secrets.CACHE_PATH):
            print("cache file is not here")
            self.client = fitbit.Fitbit(
                client_id=secrets.FITBIT_CLIENT_ID,
                client_secret=secrets.FITBIT_CLIENT_SECRET,
                redirect_uri="http://127.0.0.1:8080",
                refresh_cb=save_token_dict,
            )
        else:
            print("cache file is here")
            self.client = fitbit.Fitbit(
                client_id=secrets.FITBIT_CLIENT_ID,
                client_secret=secrets.FITBIT_CLIENT_SECRET,
                redirect_uri="http://127.0.0.1:8080",
                refresh_cb=save_token_dict,
                **load_token_dict()
            )
        self.client.API_VERSION = 1.2

    def is_client_valid(self):
        try:
            self.client.sleep()
            print("retrieved trial sleep data")
            return True
        except:
            print("retrieved trial sleep data failed")
            return False

    def send_got_client_event(self):
        self.event.set()

    async def get_client(self):
        await self.event.wait()
        return self.client

    def stop_server(self):
        self.server.cancel()

    def start_server(self):
        print("starting server")
        app = Quart(__name__)

        @app.route('/')
        async def my_form():
            url, _ = self.client.client.authorize_token_url()
            return f'''
                        <a href="{url}">redirect link</a>
                        <form method="POST">
                            <input name="text">
                        <input type="submit">
                        </form>
                        '''

        @app.route('/', methods=['POST'])
        async def my_form_post():

            form = await request.form
            text = form["text"]

            print(text)
            code = (text.split("code=")[1]).split("&state")[0]
            print(code)

            self.client.client.fetch_access_token(code)
            save_token_dict(self.client.client.session.token)
            self.send_got_client_event()

            return "done."

        self.app = app
        self.server = asyncio.create_task(app.run_task(host="0.0.0.0", debug=True))
