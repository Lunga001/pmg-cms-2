#!/usr/bin/env bash
set -e

source env/bin/activate
source production-env.sh

/var/www/pmg-cms/env/bin/newrelic-admin run-program /var/www/pmg-cms/env/bin/gunicorn -w 4 backend.app:app --bind 127.0.0.0:5005 --log-file -
