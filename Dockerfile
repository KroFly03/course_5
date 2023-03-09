FROM python:3.10

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .

RUN python -m pip install --no-cache -r requirements.txt

COPY . .

CMD gunicorn wsgi:app -b 0.0.0.0:8080 -w 4
