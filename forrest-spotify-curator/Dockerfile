ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt update && apt install ffmpeg -y

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY forrest-spotify-curator forrest-spotify-curator

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python forrest-spotify-curator/main.py)