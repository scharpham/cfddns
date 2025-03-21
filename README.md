
## Purpose

Utilizes Cloudlfare's existing python api to update dns record on whatever frequency is defined in the via the env vars in the docker compose or in a .env file you create in this directory.


## Getting started

1. Ensure docker is installed<br>
2. mkdir a new directory example 'mkdir cfddns"<br>
3. cd into directory, example 'cd cfddfs'
4. clone repo to you current working directory 'git clone' followed by the https link<br>
5. edit variables docker-compose.yml to match the cloudflare record you are trying to dynamically update<br>

**This will not likely play nicely with portainer because it lacks ability to select files in docker compose(stack)<br>
