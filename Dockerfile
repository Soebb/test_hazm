FROM python:3.11-slim-bookworm
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
COPY . ./
RUN apt-get update && apt-get -y install python3-pip build-essential
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "bot.py"]
