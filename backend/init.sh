#!/bin/bash
SCRIPT_NAME=/path gunicorn --config gunicorn_config.py wsgi:app