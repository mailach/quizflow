#!/bin/bash

while ! nc -z ksqldb-server 8088; do
  echo "Waiting for KSQLDB-server to be ready..."
  sleep 5
done

ksql http://ksqldb-server:8088 <<EOF
RUN SCRIPT '/etc/ksqldb/ksql-init.sql';
EOF

exec /bin/sh
