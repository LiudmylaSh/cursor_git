FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app/

RUN pip install Flask

# copy project
COPY . /usr/src/app/

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
