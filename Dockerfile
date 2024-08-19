FROM python:3.10-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy

COPY src ./src

ENV FLASK_APP=src.app

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.app:app"]
