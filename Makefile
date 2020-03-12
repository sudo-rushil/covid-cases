
default:
	flask run --host=0.0.0.0 --port=80

run:
	gunicorn -b 0.0.0.0:8080 app:app

build:
	docker build -t covidcases . --no-cache

start:
	docker run -d -p 8081:8080 covidcases

stop:
	docker rm $(docker stop $(docker ps -a -q  --filter ancestor=covidcases))

install:
	pip install -r requirements.txt --no-cache-dir

pull:
	git pull

deploy:
	(git pull | egrep 'up to date') || make rebuild

rebuild: pull stop build run
