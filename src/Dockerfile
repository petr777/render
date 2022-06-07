FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV HOME=/src
RUN mkdir $HOME
WORKDIR $HOME

COPY . $HOME

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker", "main:app"]

