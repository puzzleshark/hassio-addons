import asyncio

from keys_to_lights import light_show
from keys_to_lights import authentication


async def main():

    spotify_auth = authentication.SpotifyAuthenticator()
    spotify_auth.create_server()
    spotify = await spotify_auth.get_spotify()

    song_task = None
    last_song = None

    while True:
        song = spotify.currently_playing()
        if song is not None:
            if song["item"]["id"] != last_song:
                last_song = song["item"]["id"]
                info = spotify.audio_analysis(song["item"]["id"])
                if song_task is not None and not song_task.cancelled():
                    song_task.cancel()
                song_task = asyncio.create_task(light_show.light_show(info, song))
        else:
            if song_task is not None and not song_task.cancelled():
                song_task.cancel()

        await asyncio.sleep(5)

asyncio.run(main())