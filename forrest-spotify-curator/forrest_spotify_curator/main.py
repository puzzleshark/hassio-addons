import asyncio
import os

import librosa
import numpy as np

from forrest_spotify_curator import authentication
from forrest_spotify_curator import secrets


def song_in_tune(filename):
    y, sr = librosa.load(filename, duration=40)
    value = librosa.estimate_tuning(y=y, sr=sr)
    cents = round(value * 100)
    if cents < 0:
        print(f'{np.abs(cents)} cents flat')
    else:
        print(f'{np.abs(cents)} cents sharp')
    if np.abs(cents) > 9:  # needs to be better than 9 cents
        print("not good enough")
        return False
    else:
        return True


async def main():

    spotify_auth = authentication.SpotifyAuthenticator()
    spotify_auth.create_server()
    spotify = await spotify_auth.get_spotify()

    print("have spotify object")

    if not os.path.exists(secrets.MUSIC_PATH):
        os.makedirs(secrets.MUSIC_PATH)

    # filenames = download_playlist(secrets.MUSIC_PATH)

    results = spotify.playlist_items(f"spotify:playlist:{secrets.SPOTIFY_PLAYLIST_ID}")

    print("have results")

    for item in results['items']:
        track = item['track']
        print("====================================================================")
        print('track    : ' + track['name'])
        print('audio    : ' + track['uri'])

        filename = track["id"] + ".wav"

        os.system(f'spotdl {track["external_urls"]["spotify"]} -o {secrets.MUSIC_PATH} --output-format wav -p {filename}')

        try:
            if not song_in_tune(os.path.join(secrets.MUSIC_PATH, filename)):
                spotify.playlist_remove_all_occurrences_of_items(secrets.SPOTIFY_PLAYLIST_ID, [track['uri']])
                print("removed it")
        except Exception as e:
            print("could not parse, need to figure this out, removing.", e)
            spotify.playlist_remove_all_occurrences_of_items(secrets.SPOTIFY_PLAYLIST_ID, [track['uri']])

asyncio.run(main())