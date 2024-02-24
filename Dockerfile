FROM python:3.11-slim-bookworm
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt
RUN apt-get install g++
EXPOSE 5000
CMD ["python3", "bot.py"]
