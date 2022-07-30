import asyncio
import spotipy

from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler
from quart import Quart, request

from keys_to_lights import local_secrets


class SpotifyAuthenticator:

    def __init__(self):
        self.event = asyncio.Event()

        self.cache = CacheFileHandler(local_secrets.CACHE_PATH)

        self.auth = SpotifyOAuth(
            scope=["user-read-currently-playing"],
            client_id=local_secrets.SPOTIFY_CLIENT_ID,
            client_secret=local_secrets.SPOTIFY_CLIENT_SECRET,
            redirect_uri="http://localhost:8888/callback",
            open_browser=False,
            cache_handler=self.cache
        )

        self.spotify = None
        self.server = None
        self.app = None

    def set_spotify(self, spotify):
        self.spotify = spotify
        self.event.set()

    async def get_spotify(self):
        if self.cache.get_cached_token() is not None:
            self.spotify = spotipy.Spotify(oauth_manager=self.auth)
        if not self.spotify:
            await self.event.wait()
        return self.spotify

    def create_server(self):
        app = Quart(__name__)

        @app.route("/spotify")
        async def hello_world():
            return f'''
                <a href="{self.auth.get_authorize_url()}">spotify link</a>
                <form method="POST">
                    <input name="text">
                <input type="submit">
                </form>
                '''

        @app.route('/')
        async def my_form():
            return f'''
                <a href="{self.auth.get_authorize_url()}">spotify link</a>
                <form method="POST">
                    <input name="text">
                <input type="submit">
                </form>
                '''
            # return await render_template('my-form.html')

        @app.route('/', methods=['POST'])
        async def my_form_post():

            form = await request.form
            text = form["text"]

            state, auth_code = spotipy.SpotifyOAuth.parse_auth_response_url(text)
            print("auth_code", auth_code)

            self.auth.get_access_token(code=auth_code)

            spotify = spotipy.Spotify(oauth_manager=self.auth)

            self.set_spotify(spotify)

            return "done."

        self.app = app
        self.server = asyncio.create_task(app.run_task(host="0.0.0.0", debug=True))