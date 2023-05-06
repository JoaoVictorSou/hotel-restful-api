FROM debian:buster-slim
WORKDIR /app
ENV PORT=80
EXPOSE $PORT
COPY . .

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    vim

RUN pip3 install --upgrade pip==22.0.2 \
    && pip3 install -r ./requirements.txt

ENTRYPOINT python3 ./main.py
