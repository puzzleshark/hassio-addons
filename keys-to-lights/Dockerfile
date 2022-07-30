ARG BUILD_FROM
FROM $BUILD_FROM

COPY . /project
WORKDIR /project

RUN pip install -r requirements.txt

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python3 keys_to_lights/main.py)