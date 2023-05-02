FROM python:3.11
WORKDIR /app
ENV PORT=80
EXPOSE $PORT
COPY . .

RUN pip install -r ./requirements.txt

ENTRYPOINT python ./main.py
