#!/bin/bash

redis_flush() {
  redis-cli FLUSHALL
}

run_collectstatic() {
  echo "python manage.py collectstatic --noinput"
}

run_makemigrations() {
  if [[ -n $1 ]]; then
    echo "python manage.py makemigrations ${1}"
  fi
  echo "python manage.py makemigrations"
}

run_migrate() {
  echo "python manage.py migrate"
}

setup_postgres() {
  env_file="$(get_env_dir)/postgres.env"
  echo -e "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=postgres\nPOSTGRES_DB=postgres" >${env_file}
}

setup_sleekforum() {
  docker-compose exec sleekforum $(run_migrate)
  docker-compose exec sleekforum $(collectstatic)
}

stop_all_services() {
  docker-compose down
}

start_all_services() {
  docker-compose up -d
}

setup_install() {
  setup_postgres
  start_all_services
  setup_sleekforum
}
