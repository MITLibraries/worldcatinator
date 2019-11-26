FROM python:3.7-slim
ENV PIP_NO_CACHE_DIR yes
RUN \
  apt-get update -yqq && \
  pip install --upgrade pip pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --dev --system --ignore-pipfile --deploy

COPY . /app

ENTRYPOINT [ "python" ]

EXPOSE 5000
CMD ["-m", "flask", "run", "--host=0.0.0.0"]
