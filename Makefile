-include Makefile.settings
.DEFAULT_GOAL := help

run_db:
	echo "test"

db_migrate:
	DATABASE_URL=${DATABASE_URL} python manage.py db migrate

db_upgrade:
	DATABASE_URL=${DATABASE_URL} python manage.py db upgrade ${VERSION}

db_downgrade:
	DATABASE_URL=${DATABASE_URL} python manage.py db downgrade ${VERSION}

run:
	DATABASE_URL=${DATABASE_URL} BRAINTREE_DEBUG=True python run.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

help:
	echo "- run_db \n- db_migrate \n- db_upgrade \n- db_downgrade \n- run \n- clean"