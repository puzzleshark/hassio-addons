ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt update && apt install ffmpeg -y

COPY . /project
WORKDIR /project

RUN python3 -m pip install spotipy
RUN python3 -m pip install numpy
RUN python3 -m pip install librosa
RUN python3 -m pip install quart
RUN python3 -m pip install spotdl
# RUN python3 -m pip install -r requirements.txt

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python3 forrest_spotify_curator/main.py)