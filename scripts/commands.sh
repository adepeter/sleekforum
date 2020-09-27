#!/bin/bash

source utils.sh

redis_flush() {
  redis-cli FLUSHALL
}

run_collectstatic() {
  python manage.py collectstatic --noinput
}

run_makemigrations() {
  if [[ -n $1 ]]; then
    python manage.py makemigrations $1
  fi
  python manage.py makemigrations
}

run_migrate() {
  python manage.py migrate
}

setup_postgres() {
  env_file="$(get_env_dir)/postgres.env"
  echo -e "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=postgres\nPOSTGRES_DB=postgres" > ${env_file}
}

setup_sleekforum() {
  echo
}
