ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt update && apt install ffmpeg -y

COPY . /project
WORKDIR /project
RUN python3 -m pip install -r requirements.txt

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python3 forrest-spotify-curator/main.py)