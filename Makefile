all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf build && rm -rf __pycache__

venv:
	python3 -m venv venv && venv/bin/pip install -r requirements.txt

run: venv
	venv/bin/uvicorn main:app --reload --app-dir app/

test: venv
	venv/bin/python -m unittest discover -s tests

docker-build:
	docker build -t api-metadata .

docker-run:
	docker run -d --name api-metadata -p 80:80 api-metadata