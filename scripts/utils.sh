#!/bin/bash

get_project_directory() {
  echo "$(dirname $(pwd))"
}

get_env_dir() {
  base_dir="$(get_project_directory)/configs/env"
  echo "${base_dir}"
}
