
## Purpose

Utilizes Cloudlfare's existing python api to update dns record on whatever frequency is defined in the via the env vars in the docker compose or in a .env file you create in this directory.


## Getting started

Ensure docker is installed<br>
**this will not likely play nicely with portainer because it lacks ability to select files in docker compose(stack)<br>
mkdir a new directory,<br>
git clone this repo to that directory<br>
edit variables docker-compose.yml to match the record you are trying to update<br>
