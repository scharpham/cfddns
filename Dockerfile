FROM python:3.9-alpine
RUN apk update
RUN apk upgrade
RUN apk add --no-cache nano
COPY checker_updater.py .
COPY requirements.txt .
WORKDIR .
RUN pip install -r requirements.txt
CMD ["python", "-u", "./checker_updater.py"]