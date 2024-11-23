#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly cmd="$*"

: "${DB_HOST:=db}"
: "${DB_PORT:=5432}"

# We need this line to make sure that this container is started
# after the one with postgres:
wait-for-it \
  --host="$DB_HOST" \
  --port="$DB_PORT" \
  --timeout=90 \
  --strict

# It is also possible to wait for other services as well: redis, elastic, mongo
echo "Postgres ${DB_HOST}:${DB_PORT} is up"

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
