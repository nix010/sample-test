FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN python seed_data.py
RUN chmod +x ./start.sh

CMD ./start.sh