
[Purpose]:
Utilizes Cloudlfare's existing python api to update dns record on whatever frequency is defined in the .env file
can be run locally on a cron job or in docker

[Getting started]:
Ensure docker is installed
**this will not likely play nicely with portainer because it lacks ability to select files in docker compose(stack)
mkdir a new directory,
git clone this repo to that directory
edit variables docker-compose.yml to match the record you are trying to update
