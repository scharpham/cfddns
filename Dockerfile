FROM python:3.9-alpine
RUN apk update
RUN apk upgrade
COPY checker_updater.py .
CMD ['python3', './checker_updater.py']