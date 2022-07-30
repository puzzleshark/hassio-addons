ARG BUILD_FROM
FROM $BUILD_FROM

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY sleep_tracker sleep_tracker

CMD (export PYTHONPATH=$PWD:$PYTHONPATH && python sleep_tracker/main.py)