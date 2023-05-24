FROM python:3.11.2-alpine 

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt 

COPY . /app/

CMD ["python","bot.py"]