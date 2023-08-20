# shop-projectV3
Final Django project. Clothes shop

All actions should be executed from the source directory of the project and only after installing all requirements.

1.Firstly, create and activate a new virtual environment:

python3.11 -m venv ../venv source ../venv/bin/activate

2.Install packages:

pip install --upgrade pip pip install -r requirements.txt

3.Run project dependencies, migrations, fill the database with the fixture data etc.:

./manage.py migrate ./manage.py loaddata <path_to_fixture_files> ./manage.py runserver

4.Run Redis Server:

5.redis-server Run Celery:

celery -A store worker --loglevel=INFO