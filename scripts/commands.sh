#!/bin/bash

source ./validators.sh

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
  echo -e "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=postgres" > ${env_file}
  echo -e "POSTGRES_DB=postgres" >> ${env_file}
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

start_service_by_name() {
  test -z $1 && echo "You must supply a service name"; exit 1
  validate_service $1
  if [[ $? -eq 0 ]]; then
    docker-compose start $1
  fi
}

stop_service_by_name() {
  test -z $1 && echo "You must supply a service name to terminate"; exit 1
  validate_service $1
  if [[ $? -eq 0 ]]; then
    docker-compose stop $1
  fi
}

setup_install() {
  setup_postgres
  start_all_services
  setup_sleekforum
}
