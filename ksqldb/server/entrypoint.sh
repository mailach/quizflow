#!/bin/bash
while ! nc -z kafka 9092; do
  echo "Waiting for Kafka to be ready..."
  sleep 1
done

bash -c "/usr/bin/docker/run" 