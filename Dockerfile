# app/Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY ./ /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8000"]