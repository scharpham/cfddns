FROM python:3.9-alpine
ARG CLOUDFLARE_EMAIL $CLOUDFLARE_EMAIL
ARG CLOUDFLARE_API_KEY $CLOUDFLARE_API_KEY
ARG ZONE_ID $ZONE_ID
ARG DNS_RECORD_ID $DNS_RECORD_ID
ARG NAME $NAME
ARG TYPE $TYPE
ARG UPDATE_FREQUENCY_MIN $UPDATE_FREQUENCY_MIN
RUN apk update
RUN apk upgrade
COPY checker_updater.py .
COPY requirements.txt .
COPY .env .
WORKDIR .
RUN pip install -r requirements.txt
CMD ["python", "./checker_updater.py"]