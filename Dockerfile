FROM python:3.11.3-bullseye
WORKDIR /app

RUN apt update && apt install -y netcat

ENV FLASK_HOST="0.0.0.0"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "/app/check.sh" ]
# RUN sh -c python create_db.py
# RUN export FLASK_APP=app.py 
# RUN flask db init && flask db migrate && flask db upgrade
EXPOSE 5000
CMD ["python3", "app.py"]