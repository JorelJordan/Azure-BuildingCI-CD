setup:
	python3 -m venv ~/.udacity-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		

test:
	python -m pytest -vv testapp.py

	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile 
	pylint app.py

all: setup install lint test
