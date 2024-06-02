FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

# Eksponuj port, na którym działa aplikacja Flask
EXPOSE 5000

# Uruchom aplikację Flask za pomocą flask run
CMD ["flask", "run", "--host=0.0.0.0"]
