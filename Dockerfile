FROM python:3.9
RUN apk update
RUN apk upgrade
COPY checker_updater.py .

CMD ['python', './checker_updater.py']