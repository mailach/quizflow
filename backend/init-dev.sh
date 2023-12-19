#!/bin/bash
while ! nc -z ksqldb-server 8088; do
  echo "Waiting for KSQLDB-server to be ready..."
  sleep 5
done

flask --debug run --host 0.0.0.0   