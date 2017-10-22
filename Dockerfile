FROM python:3

WORKDIR /usr/src/app

ADD ./src ./src
ADD ./tests ./tests

CMD [ "python", "./tests/test_main.py" ]