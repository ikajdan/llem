FROM python:3.12-slim

WORKDIR /app

COPY ./app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY model /model
COPY app /app

RUN groupadd -g 1000 gunicorn \
    && useradd -m -u 1000 -g gunicorn gunicorn \
    && chown -R gunicorn:gunicorn /app

USER gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

HEALTHCHECK CMD curl --fail 0.0.0.0:5000 || exit 1
