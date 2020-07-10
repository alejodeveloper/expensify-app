build-docker-dev:
	cp -a expensify/ docker/dev/expensify
	cd docker/dev/ && docker build -t "expensify-app/dev" .
	rm -rf docker/dev/expensify

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop
