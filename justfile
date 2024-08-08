# run local server
preview:
  poetry run python manage.py runserver

# make migrations
mm:
  poetry run python manage.py makemigrations

# migrate
migrate:
  poetry run python manage.py migrate
