#!/bin/bash

set -e

#host="$1"
#shift
#
#until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c '\q'; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done
#
#>&2 echo "Postgres is up - executing command"
#exec ""
echo 'start'
sleep 5
psql -U postgres -d dev_db -c  "CREATE SCHEMA IF NOT EXISTS my_schema2 AUTHORIZATION postgres"
echo 'uraa'
