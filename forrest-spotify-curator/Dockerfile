ARG BUILD_FROM
FROM $BUILD_FROM

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY forrest-spotify-curator /forrest-spotify-curator

CMD python forrest-spotify-curator/main.py