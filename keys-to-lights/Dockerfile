ARG BUILD_FROM
FROM $BUILD_FROM

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY keys_to_lights /keys_to_lights

CMD python /keys_to_lights/main.py