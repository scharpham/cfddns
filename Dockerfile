FROM python:3.9-alpine
RUN apk update
RUN apk upgrade
COPY checker_updater.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "./checker_updater.py"]