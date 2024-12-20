docker-compose stop web
docker-compose rm -f web
docker-compose build web
docker-compose up -d web
