
## Purpose

Utilizes Cloudlfare's existing python api to update dns record on whatever frequency is defined in the via the env vars in the docker compose or in a .env file you create in this directory.


## Getting started

1. Ensure docker is installed<br>
2. mkdir a new directory example 'mkdir cfddns"<br>
3. cd into directory, example 'cd cfddfs'
4. clone repo to your current working directory 'git clone' followed by the https link<br>
5. edit variables docker-compose.yml to match the cloudflare record you are trying to dynamically update<br>

6. To test is its fuctionioning correctly first run compose file in attached mode 'sudo docker compose up'
7. If setup correctly it will start by showing you the current ip for your dns record, and try to update
8. If no update you will see "no change" followed by the date
9. If update, you will see "updated" followed by the date
10. If error, you will see "errored" followed by the date

11. After confirming you can connect in attached mode, stop container 'sudo docker compose down'
12. Re run  in detached mode, 'sudo docker compose up -d'
13. You should be good to go!

**This will not likely play nicely with portainer because it lacks ability to select files in docker compose(stack)<br>
