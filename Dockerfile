FROM python:alpine

USER root

COPY data_types/ /root/data_types/
COPY tests/ /root/tests/

RUN pip install pytest

ENV PYTHONPATH=/root

WORKDIR /root

ENTRYPOINT pytest -v tests/
