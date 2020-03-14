
default:
	flask run --host=0.0.0.0 --port=80

run:
	gunicorn -w 2 -b 0.0.0.0:8080 app:app

build:
	docker build -t covidcases . --no-cache

start:
	docker run -d -p 8081:8080 --name="covidcases" covidcases

stop:
	docker stop covidcases
	docker rm covidcases
	docker image prune -a

install:
	pip install -r requirements.txt --no-cache-dir

pull:
	git pull

deploy:
	(git pull | egrep 'up to date') || make rebuild

rebuild: pull stop build run
