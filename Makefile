create_venv:
	python3 -m venv .venv

activate_venv: create_venv
	. .venv/bin/activate

install_reqs: activate_venv
	pip install -r requiremets.txt --quiet

run: install_reqs
	python3 main.py $(realpath index.html)

all: run
