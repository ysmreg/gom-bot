FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y ffmpeg cmake gcc open-jtalk

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
COPY tts-requirements.txt .

RUN pipenv install
RUN pipenv install -r tts-requirements.txt

COPY . /usr/src/app

CMD ["pipenv", "run", "python3", "main.py"]
