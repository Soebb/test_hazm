FROM python:3.11-slim-bookworm
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
#COPY requirements.txt ./requirements.txt
COPY . ./
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "bot.py"]
