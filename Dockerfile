# Comparison of various python Docker images
#
# python                   2.7                  17c0fe4e76a5        5 weeks ago         908MB
# python                   2.7-alpine           5082b69714da        12 days ago         60.1MB
# python                   2.7-slim             40792d8a2d6d        4 weeks ago         120MB
# python                   2-stretch            17c0fe4e76a5        5 weeks ago         908MB
# python                   3                    825141134528        4 weeks ago         923MB
# python                   3-alpine             f3f1da982c36        12 days ago         79.4MB
# python                   3-slim               4c2534c95211        4 weeks ago         143MB
# python                   3-stretch            825141134528        4 weeks ago         923MB
# python                   alpine               f3f1da982c36        12 days ago         79.4MB
# python                   slim                 4c2534c95211        4 weeks ago         143MB

FROM python:3-alpine

USER root

COPY data_types.py /root/
COPY tests/ /root/tests/

RUN pip install pytest

WORKDIR /root

# Run pytest with python 3
ENTRYPOINT python -m pytest -v tests/

# Run pytest with python 2.7
#ENTRYPOINT pytest -v tests/
