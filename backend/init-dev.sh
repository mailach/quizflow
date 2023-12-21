#!/bin/bash
while ! nc -z kafka 9092; do
  echo "Waiting for Kafka to be ready..."
  sleep 1
done

while ! nc -z ksqldb-server 8088; do
  echo "Waiting for KSQLDB-server to be ready..."
  sleep 1
done

flask --debug run --host 0.0.0.0   