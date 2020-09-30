#!/bin/bash

validate_service() {
  local SLEEKFORUM_SERVICES=("sleekforum" "nginx" "postgres")
  test -z ${1} && echo "You must supply a service name"; exit 1
  test ${#} -gt 1 && echo "You can only validate a service"; exit 1
  test ${#} -lt 1 && echo "You must provide a service name"; exit 1
  for service in ${SLEEKFORUM_SERVICES[@]}; do
    if [[ ${service} == ${1,,} ]]; then
      return 0
    fi
  done
  return 1
}