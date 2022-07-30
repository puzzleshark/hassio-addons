ARG BUILD_FROM
FROM $BUILD_FROM

COPY . /project
WORKDIR /project

RUN python3 -m pip install -r requirements.txt

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python3 sleep_tracker/main.py)